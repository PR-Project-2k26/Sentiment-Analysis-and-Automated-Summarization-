import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def evaluate_ai_content(resume_text):

    prompt = f"""
You are a senior ATS recruiter, resume reviewer and technical hiring manager.

Analyze ONLY the WRITING QUALITY of the resume.

Do NOT evaluate job matching.

Evaluate the resume in these categories:

1. Grammar
2. Professional Tone
3. Clarity
4. Readability
5. Conciseness
6. Achievement Impact
7. Bullet Quality
8. Verb Variety
9. Keyword Optimization
10. Project Description Quality
11. Resume Consistency
12. Quantification of Achievements
13. ATS Friendly Writing

For EACH category provide:
- score (0-10)
- reason

Finally provide 5 actionable suggestions.

Return ONLY valid JSON in this exact format:

{{
    "grammar":{{"score":0,"reason":""}},
    "professional_tone":{{"score":0,"reason":""}},
    "clarity":{{"score":0,"reason":""}},
    "readability":{{"score":0,"reason":""}},
    "conciseness":{{"score":0,"reason":""}},
    "achievement_impact":{{"score":0,"reason":""}},
    "bullet_quality":{{"score":0,"reason":""}},
    "verb_variety":{{"score":0,"reason":""}},
    "keyword_optimization":{{"score":0,"reason":""}},
    "project_quality":{{"score":0,"reason":""}},
    "resume_consistency":{{"score":0,"reason":""}},
    "quantification":{{"score":0,"reason":""}},
    "ats_writing":{{"score":0,"reason":""}},
    "feedback":[
        "",
        "",
        "",
        "",
        ""
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
            response_format={"type": "json_object"},
            temperature=0.2
        )

        return json.loads(
            completion.choices[0].message.content
        )

    except Exception as e:

        return {

            "grammar":{"score":5,"reason":str(e)},
            "professional_tone":{"score":5,"reason":""},
            "clarity":{"score":5,"reason":""},
            "readability":{"score":5,"reason":""},
            "conciseness":{"score":5,"reason":""},
            "achievement_impact":{"score":5,"reason":""},
            "bullet_quality":{"score":5,"reason":""},
            "verb_variety":{"score":5,"reason":""},
            "keyword_optimization":{"score":5,"reason":""},
            "project_quality":{"score":5,"reason":""},
            "resume_consistency":{"score":5,"reason":""},
            "quantification":{"score":5,"reason":""},
            "ats_writing":{"score":5,"reason":""},
            "feedback":[]
        }