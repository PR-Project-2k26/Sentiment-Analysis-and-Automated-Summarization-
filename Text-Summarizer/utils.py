from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text):
    try:
        prompt = f"""
        Analyze the following text and generate:

        1. SUMMARY: A concise summary
        2. EMOTION: Overall tone (Positive, Negative, Neutral, Critical, etc.)
        3. KEY TOPICS: Bullet points of main topics
        4. KEYWORDS: Important keywords
        5. READABILITY: Level (Beginner, Intermediate, Advanced) with explanation

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

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an intelligent text analysis assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {str(e)}"