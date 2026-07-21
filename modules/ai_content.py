import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def evaluate_ai_content(resume_text):
    """
    AI-powered evaluation of resume writing quality.

    Returns:
    {
        "grammar": 8,
        "professional_tone": 9,
        "clarity": 8,
        "readability": 9,
        "feedback": [...]
    }
    """

    prompt = f"""
You are an expert ATS recruiter and resume writing expert.

Analyze ONLY the WRITING QUALITY of the resume below.

Evaluate the following categories from 0 to 10.

1. Grammar
2. Professional Tone
3. Clarity
4. Readability
5. Conciseness
6. Achievement Impact
7. Bullet Point Quality
8. Verb Variety

For every category provide:
- score
- reason

Finally provide 5 actionable suggestions.

Return ONLY valid JSON in the following format.

{{
    "grammar": {{
        "score": 8,
        "reason": "Minor punctuation issues."
    }},
    "professional_tone": {{
        "score": 9,
        "reason": "Professional language is consistent."
    }},
    "clarity": {{
        "score": 8,
        "reason": "Most bullet points are easy to understand."
    }},
    "readability": {{
        "score": 9,
        "reason": "Resume is easy to scan."
    }},
    "conciseness": {{
        "score": 8,
        "reason": "Some bullet points are slightly long."
    }},
    "achievement_impact": {{
        "score": 7,
        "reason": "More quantified achievements are needed."
    }},
    "bullet_quality": {{
        "score": 8,
        "reason": "Most bullets begin with strong action verbs."
    }},
    "verb_variety": {{
        "score": 6,
        "reason": "Action verbs are repeated too often."
    }},
    "feedback": [
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}

Resume:

{resume_text}
"""
    try:

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )

        response = completion.choices[0].message.content

        return json.loads(response)

    except Exception as e:

        return {
            "grammar": {
                "score": 5,
                "reason": str(e)
            },
            "professional_tone": {
                "score": 5,
                "reason": ""
            },
            "clarity": {
                "score": 5,
                "reason": ""
            },
            "readability": {
                "score": 5,
                "reason": ""
            },
            "conciseness": {
                "score": 5,
                "reason": ""
            },
            "achievement_impact": {
                "score": 5,
                "reason": ""
            },
            "bullet_quality": {
                "score": 5,
                "reason": ""
            },
            "verb_variety": {
                "score": 5,
                "reason": ""
            },
            "overall": {
                "score": 5,
                "reason": "AI evaluation failed."
            },
            "strengths": [],
            "feedback": []
        }