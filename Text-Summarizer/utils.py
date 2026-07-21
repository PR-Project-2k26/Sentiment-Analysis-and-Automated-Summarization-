import os
import re
import time
import math

from groq import Groq
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
_vader = SentimentIntensityAnalyzer()

# ---------------------------------------------------------------------------
# Length presets: controls how the prompt asks the LLM to size the summary
# ---------------------------------------------------------------------------
LENGTH_PRESETS = {
    "Short": "in 2-3 sentences (roughly 40-60 words)",
    "Medium": "in 4-6 sentences (roughly 80-120 words)",
    "Long": "in 8-10 sentences (roughly 180-250 words)",
}


def _build_prompt(text, length="Medium"):
    length_instruction = LENGTH_PRESETS.get(length, LENGTH_PRESETS["Medium"])
    return f"""
Analyze the following text and generate:

1. SUMMARY: A concise summary, written {length_instruction}.
2. EMOTION: Overall tone (Positive, Negative, Neutral, Critical, etc.)
3. KEY TOPICS: Bullet points of main topics
4. KEYWORDS: 5-10 important keywords, comma-free, one per line
5. READABILITY: Level (Beginner, Intermediate, Advanced) with a one-line explanation

Text:
{text}

Format strictly like:

SUMMARY:
...

EMOTION:
...

KEY TOPICS:
- ...
- ...

KEYWORDS:
- ...
- ...

READABILITY:
...
"""


# ---------------------------------------------------------------------------
# Parsing: turn the LLM's semi-structured text into a clean dict so the UI
# can render each section separately instead of one big blob.
# ---------------------------------------------------------------------------
def parse_llm_response(raw_text):
    sections = {"summary": "", "emotion": "", "topics": [], "keywords": [], "readability": ""}
    if not raw_text:
        return sections

    pattern = r"(SUMMARY|EMOTION|KEY TOPICS|KEYWORDS|READABILITY):"
    parts = re.split(pattern, raw_text)
    # re.split with a capturing group returns [pre, tag, content, tag, content, ...]
    it = iter(parts[1:])
    for tag, content in zip(it, it):
        content = content.strip()
        tag = tag.strip().upper()
        if tag == "SUMMARY":
            sections["summary"] = content
        elif tag == "EMOTION":
            sections["emotion"] = content.splitlines()[0].strip() if content else ""
        elif tag == "KEY TOPICS":
            sections["topics"] = [
                line.lstrip("-• ").strip() for line in content.splitlines() if line.strip()
            ]
        elif tag == "KEYWORDS":
            sections["keywords"] = [
                line.lstrip("-• ").strip() for line in content.splitlines() if line.strip()
            ]
        elif tag == "READABILITY":
            sections["readability"] = content.strip()

    if not sections["summary"]:
        # Fallback: model didn't follow formatting, just use raw text
        sections["summary"] = raw_text.strip()
    return sections


# ---------------------------------------------------------------------------
# Local (non-LLM) sentiment scoring via VADER — fast, free, deterministic.
# Used alongside the LLM's own EMOTION label for the dashboard chart.
# ---------------------------------------------------------------------------
def get_sentiment_scores(text):
    scores = _vader.polarity_scores(text)
    return {
        "positive": round(scores["pos"] * 100, 1),
        "neutral": round(scores["neu"] * 100, 1),
        "negative": round(scores["neg"] * 100, 1),
        "compound": round(scores["compound"], 3),
    }


def sentiment_label_from_compound(compound):
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    return "Neutral"


# ---------------------------------------------------------------------------
# Text statistics: word/sentence counts, reading time, compression ratio
# ---------------------------------------------------------------------------
def get_text_stats(original_text, summary_text):
    def word_count(t):
        return len(re.findall(r"\b\w+\b", t))

    def sentence_count(t):
        return max(1, len(re.findall(r"[.!?]+(?:\s|$)", t)))

    orig_words = word_count(original_text)
    summ_words = word_count(summary_text)
    compression = round((1 - summ_words / orig_words) * 100, 1) if orig_words else 0.0

    return {
        "original_words": orig_words,
        "summary_words": summ_words,
        "original_sentences": sentence_count(original_text),
        "summary_sentences": sentence_count(summary_text),
        "compression_pct": compression,
        "reading_time_original_sec": math.ceil(orig_words / (200 / 60)),  # 200 wpm
        "reading_time_summary_sec": math.ceil(summ_words / (200 / 60)),
    }


# ---------------------------------------------------------------------------
# Word cloud generation from keywords (falls back to summary text)
# ---------------------------------------------------------------------------
def generate_wordcloud_image(keywords, fallback_text=""):
    text_for_cloud = " ".join(keywords) if keywords else fallback_text
    if not text_for_cloud.strip():
        return None
    wc = WordCloud(width=800, height=400, background_color="white", colormap="viridis")
    wc.generate(text_for_cloud)
    return wc.to_image()


# ---------------------------------------------------------------------------
# Main entry point used by app.py and main.py
# ---------------------------------------------------------------------------
def summarize_text(text, length="Medium", return_raw=False):
    """
    Returns a dict:
    {
        summary, emotion, topics, keywords, readability,
        sentiment: {positive, neutral, negative, compound},
        stats: {...},
        latency_sec, error (optional)
    }
    """
    result = {
        "summary": "", "emotion": "", "topics": [], "keywords": [], "readability": "",
        "sentiment": {}, "stats": {}, "latency_sec": 0.0, "error": None,
    }

    start = time.time()
    try:
        prompt = _build_prompt(text, length)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an intelligent text analysis assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        raw = response.choices[0].message.content
        parsed = parse_llm_response(raw)
        result.update(parsed)
        if return_raw:
            result["raw"] = raw
    except Exception as e:
        result["error"] = str(e)
        result["summary"] = f"Error occurred: {str(e)}"

    result["latency_sec"] = round(time.time() - start, 2)
    result["sentiment"] = get_sentiment_scores(text)
    result["stats"] = get_text_stats(text, result["summary"])
    return result
