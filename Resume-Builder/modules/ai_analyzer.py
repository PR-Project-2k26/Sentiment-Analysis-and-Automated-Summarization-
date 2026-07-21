import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume_ai(resume_text, job_description):

    prompt = f"""
You are an experienced recruiter.

Analyze this resume according to the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return your answer in markdown under these headings:

## Overall Summary
## Strengths
## Weaknesses
## Missing Skills
## Recruiter Feedback
## Final Recommendation
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content