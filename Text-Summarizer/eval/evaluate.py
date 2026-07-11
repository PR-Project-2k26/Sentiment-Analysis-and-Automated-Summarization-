"""
Evaluation harness for the Text Summarizer project.

Measures two things, since this project isn't a trained classifier with a
single "accuracy" number by default:

1. Summary quality  -> ROUGE-1 / ROUGE-2 / ROUGE-L (F-measure) against
   hand-written reference summaries in eval/test_data.json.
2. Sentiment accuracy -> compares the predicted sentiment label (from VADER,
   deterministic, and optionally from the LLM's own EMOTION field) against
   a ground-truth label, and reports accuracy as a percentage.

Usage:
    python eval/evaluate.py            # real run, needs GROQ_API_KEY in .env
    python eval/evaluate.py --mock     # offline dry-run to sanity check the
                                        # harness itself (no API calls)

Results are printed as a table and saved to eval/results.csv.
"""

import argparse
import csv
import json
import os
import sys

from rouge_score import rouge_scorer

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_sentiment_scores, sentiment_label_from_compound  # noqa: E402


def mock_summarize(text, length="Medium"):
    """
    Offline stand-in for utils.summarize_text, used only with --mock.
    Does a naive extractive 'summary' (first 2 sentences) so the ROUGE /
    accuracy plumbing can be tested without calling the real API.
    """
    import re
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    summary = " ".join(sentences[:2])
    sentiment = get_sentiment_scores(text)
    return {
        "summary": summary,
        "emotion": sentiment_label_from_compound(sentiment["compound"]),
        "topics": [],
        "keywords": [],
        "readability": "Intermediate",
        "sentiment": sentiment,
        "stats": {},
        "latency_sec": 0.0,
        "error": None,
    }


def normalize_emotion_label(label):
    """Map free-text LLM emotion labels (e.g. 'Critical', 'Mixed') down to
    the 3-way Positive/Negative/Neutral scale used by the ground truth."""
    if not label:
        return "Neutral"
    label = label.lower()
    if any(w in label for w in ["positive", "hopeful", "optimistic", "excited"]):
        return "Positive"
    if any(w in label for w in ["negative", "critical", "concern", "angry", "sad"]):
        return "Negative"
    return "Neutral"


def run_evaluation(use_mock=False):
    data_path = os.path.join(os.path.dirname(__file__), "test_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        samples = json.load(f)

    if use_mock:
        summarize_fn = mock_summarize
    else:
        from utils import summarize_text as summarize_fn  # requires GROQ_API_KEY

    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)

    rows = []
    rouge1_scores, rouge2_scores, rougeL_scores = [], [], []
    vader_correct, llm_correct, total = 0, 0, 0

    for sample in samples:
        result = summarize_fn(sample["text"], length="Medium")

        if result.get("error"):
            print(f"[{sample['id']}] ERROR: {result['error']} (skipped)")
            continue

        scores = scorer.score(sample["reference_summary"], result["summary"])
        r1, r2, rl = scores["rouge1"].fmeasure, scores["rouge2"].fmeasure, scores["rougeL"].fmeasure
        rouge1_scores.append(r1)
        rouge2_scores.append(r2)
        rougeL_scores.append(rl)

        vader_pred = sentiment_label_from_compound(result["sentiment"]["compound"])
        llm_pred = normalize_emotion_label(result.get("emotion", ""))
        true_label = sample["true_sentiment"]

        vader_hit = vader_pred == true_label
        llm_hit = llm_pred == true_label
        vader_correct += int(vader_hit)
        llm_correct += int(llm_hit)
        total += 1

        rows.append({
            "id": sample["id"],
            "rouge1": round(r1, 3),
            "rouge2": round(r2, 3),
            "rougeL": round(rl, 3),
            "true_sentiment": true_label,
            "vader_pred": vader_pred,
            "vader_correct": vader_hit,
            "llm_pred": llm_pred,
            "llm_correct": llm_hit,
        })

    # --- Print table ---
    print(f"\n{'ID':<14}{'ROUGE-1':<9}{'ROUGE-2':<9}{'ROUGE-L':<9}{'True':<10}{'VADER':<10}{'LLM':<10}")
    for r in rows:
        print(f"{r['id']:<14}{r['rouge1']:<9}{r['rouge2']:<9}{r['rougeL']:<9}"
              f"{r['true_sentiment']:<10}{r['vader_pred']:<10}{r['llm_pred']:<10}")

    if total:
        print("\n--- Summary quality (ROUGE F-measure, averaged) ---")
        print(f"ROUGE-1: {sum(rouge1_scores)/total:.3f}")
        print(f"ROUGE-2: {sum(rouge2_scores)/total:.3f}")
        print(f"ROUGE-L: {sum(rougeL_scores)/total:.3f}")

        print("\n--- Sentiment accuracy ---")
        print(f"VADER (local, deterministic): {vader_correct}/{total} = {vader_correct/total*100:.1f}%")
        print(f"LLM EMOTION field:            {llm_correct}/{total} = {llm_correct/total*100:.1f}%")
    else:
        print("No samples were successfully evaluated (all errored out).")

    # --- Save CSV ---
    out_path = os.path.join(os.path.dirname(__file__), "results.csv")
    if rows:
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nSaved detailed results to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock", action="store_true",
                         help="Run offline with a naive extractive summarizer "
                              "instead of calling the Groq API (for testing the harness).")
    args = parser.parse_args()
    run_evaluation(use_mock=args.mock)
