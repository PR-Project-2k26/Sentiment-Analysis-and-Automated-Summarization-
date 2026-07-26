import os
from dotenv import load_dotenv
from groq import Groq
from PyPDF2 import PdfReader

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ----------------------------------------------------
# Extract text from uploaded PDF
# ----------------------------------------------------
def extract_text_from_pdf(file):
    """
    Extract text from an uploaded PDF file.
    Accepts Flask's FileStorage object.
    """

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


# ----------------------------------------------------
# Split text into paragraph-based chunks
# ----------------------------------------------------
def split_text(text, chunk_size=6000):
    """
    Splits text into chunks while trying to preserve
    paragraph boundaries instead of cutting sentences.
    """

    paragraphs = text.split("\n")

    chunks = []
    current_chunk = ""

    for para in paragraphs:

        para = para.strip()

        if not para:
            continue

        # If paragraph itself is extremely large,
        # split it safely.
        if len(para) > chunk_size:

            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""

            for i in range(0, len(para), chunk_size):
                chunks.append(para[i:i + chunk_size])

            continue

        if len(current_chunk) + len(para) + 1 <= chunk_size:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


# ----------------------------------------------------
# Summarize one chunk
# ----------------------------------------------------
def summarize_chunk(chunk):
    """
    Summarize a single chunk using Groq.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional document summarizer. "
                    "Generate a concise summary while preserving all important facts, "
                    "key points, names, dates, statistics and conclusions."
                ),
            },
            {
                "role": "user",
                "content": f"Summarize the following document:\n\n{chunk}",
            },
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()


# ----------------------------------------------------
# Summarize large PDFs
# ----------------------------------------------------
def summarize_large_text(text, chunk_size=6000):
    """
    Splits large PDFs into chunks, summarizes each,
    then summarizes the combined summaries.
    """

    if not text.strip():
        raise ValueError("No text found inside the PDF.")

    chunks = split_text(text, chunk_size)

    partial_summaries = []

    for chunk in chunks:
        try:
            summary = summarize_chunk(chunk)
            partial_summaries.append(summary)

        except Exception as e:
            raise Exception(f"Error summarizing PDF: {str(e)}")

    if len(partial_summaries) == 1:
        return partial_summaries[0]

    combined_summary = "\n\n".join(partial_summaries)

    try:
        final_summary = summarize_chunk(combined_summary)
    except Exception as e:
        raise Exception(f"Error generating final summary: {str(e)}")

    return final_summary