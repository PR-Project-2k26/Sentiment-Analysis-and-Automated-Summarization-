import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_career_roadmap(
    resume_text,
    job_description,
    missing_skills
):

    missing = ", ".join(sorted(missing_skills))

    prompt = f"""
You are a senior software engineering career mentor.

The candidate wants to apply for:

Below is the resume.

{resume_text}

Below is the Job Description.

{job_description}

Missing Skills:

{missing}

Generate a personalized career roadmap.

Instructions:

1. Create a practical 4-week roadmap.
2. Prioritize the missing skills.
3. Recommend projects instead of only courses.
4. Suggest high-quality learning resources such as:
- freeCodeCamp
- MDN
- Microsoft Learn
- AWS Skill Builder
- Google Cloud Skills Boost
- FastAPI official documentation
- Docker official documentation
- Roadmap.sh
- LeetCode (when appropriate)
- GeeksforGeeks (only for revision)
5. Recommend certifications ONLY if they add significant value.
6. Suggest DSA practice if required.
7. Recommend resume improvements.
8. Keep the roadmap realistic for a college student.
9. Finish with:
   - Expected Resume Improvement
   - Expected Interview Readiness
   - Final Motivation

Return the answer in Markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content