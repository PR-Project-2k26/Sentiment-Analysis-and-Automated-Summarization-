import os
import textwrap

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def summarize_chunk(text):

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": """
You are an expert document summarizer.

Your task is to generate a concise and informative summary.

Rules:

- Use bullet points.
- Preserve important facts.
- Keep names, numbers and dates.
- Remove unnecessary repetition.
- Use professional language.
- Do not add information that is not present.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content


def summarize_large_text(text):

    chunks = textwrap.wrap(
        text,
        width=2500,
        break_long_words=False,
        replace_whitespace=False
    )

    chunk_summaries = []

    for chunk in chunks:
        chunk_summaries.append(
            summarize_chunk(chunk)
        )

    combined_summary = "\n".join(chunk_summaries)

    final_summary = summarize_chunk(combined_summary)

    return final_summary