from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_chunk(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Summarize the following text in bullet points."},
            {"role": "user", "content": text}
        ],
    )
    return response.choices[0].message.content


def summarize_large_text(text):
    chunks = [text[i:i+2000] for i in range(0, len(text), 2000)]
    summaries = [summarize_chunk(chunk) for chunk in chunks]
    return "\n".join(summaries)