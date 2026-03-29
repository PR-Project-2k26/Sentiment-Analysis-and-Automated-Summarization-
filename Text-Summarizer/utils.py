from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # updated working model
            messages=[
                {"role": "system", "content": "Summarize the text clearly and concisely."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {str(e)}"