import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_job_match(resume_text, job_description):

    prompt = f"""
You are an expert ATS recruiter.

Compare the Resume with the Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON.

{{
    "technical_skills": {{
        "matched": [],
        "missing": []
    }},

    "frameworks_tools": {{
        "matched": [],
        "missing": []
    }},

    "projects": {{
        "quality":"Excellent",
        "reason":"",
        "technologies_used":[],
        "strengths":[],
        "weaknesses":[]
    }},

    "experience": {{
        "quality":"Good",
        "reason":"",
        "matched_domains":[]
    }},

    "skill_evidence": {{
        "supported_skills":[],
        "unsupported_skills":[]
    }},

    "action_words": {{
        "strong":[],
        "weak":[]
    }}
}}
"""

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

    data = json.loads(
        completion.choices[0].message.content
    )

    return calculate_job_match_score(data)


def calculate_job_match_score(data):

    technical = data.get(
        "technical_skills",
        {
            "matched": [],
            "missing": []
        }
    )

    frameworks = data.get(
        "frameworks_tools",
        {
            "matched": [],
            "missing": []
        }
    )

    projects = data.get(
        "projects",
        {}
    )

    experience = data.get(
        "experience",
        {}
    )

    evidence = data.get(
        "skill_evidence",
        {}
    )

    action = data.get(
        "action_words",
        {}
    )

    # -------------------------
    # Technical Skills (15)
    # -------------------------

    total = (
        len(technical["matched"])
        + len(technical["missing"])
    )

    if total == 0:
        technical_score = 0
    else:
        technical_score = round(
            len(technical["matched"])
            / total
            * 15
        )

    # -------------------------
    # Frameworks (8)
    # -------------------------

    total = (
        len(frameworks["matched"])
        + len(frameworks["missing"])
    )

    if total == 0:
        framework_score = 0
    else:
        framework_score = round(
            len(frameworks["matched"])
            / total
            * 8
        )

    # -------------------------
    # Projects (7)
    # -------------------------

    mapping = {

        "Excellent": 7,

        "Good": 5,

        "Average": 3,

        "Poor": 1

    }

    project_quality = projects.get(
        "quality",
        "Poor"
    )

    project_score = mapping.get(
        project_quality,
        1
    )

    # -------------------------
    # Experience (5)
    # -------------------------

    mapping = {

        "Excellent": 5,

        "Good": 4,

        "Average": 2,

        "Poor": 1

    }

    experience_quality = experience.get(
        "quality",
        "Poor"
    )

    experience_score = mapping.get(
        experience_quality,
        1
    )

    # -------------------------
    # Action Words (5)
    # -------------------------

    strong = action.get(
        "strong",
        []
    )

    weak = action.get(
        "weak",
        []
    )

    if len(strong) >= 10:
        action_score = 5

    elif len(strong) >= 7:
        action_score = 4

    elif len(strong) >= 5:
        action_score = 3

    elif len(strong) >= 3:
        action_score = 2

    else:
        action_score = 1

    supported = evidence.get(
        "supported_skills",
        []
    )

    unsupported = evidence.get(
        "unsupported_skills",
        []
    )

    if len(supported) + len(unsupported):

        ratio = len(supported) / (
            len(supported)
            + len(unsupported)
        )

        if ratio >= 0.9:
            action_score += 1

        elif ratio <= 0.4:
            action_score -= 1

    action_score = max(
        0,
        min(action_score, 5)
    )

    total_score = (

        technical_score

        + framework_score

        + project_score

        + experience_score

        + action_score

    )

    return {

        "score": total_score,

        "technical": {
            "matched": technical["matched"],
            "missing": technical["missing"],
            "score": technical_score
        },

        "frameworks": {
            "matched": frameworks["matched"],
            "missing": frameworks["missing"],
            "score": framework_score
        },

        "projects": {
            "score": project_score,
            "quality": project_quality,
            "reason": projects.get(
                "reason",
                ""
            ),
            "technologies_used": projects.get(
                "technologies_used",
                []
            ),
            "strengths": projects.get(
                "strengths",
                []
            ),
            "weaknesses": projects.get(
                "weaknesses",
                []
            )
        },

        "experience": {
            "score": experience_score,
            "quality": experience_quality,
            "reason": experience.get(
                "reason",
                ""
            ),
            "matched_domains": experience.get(
                "matched_domains",
                []
            )
        },

        "action": {
            "keywords": strong,
            "strong": strong,
            "weak": weak,
            "score": action_score
        },

        "evidence": {
            "supported_skills": supported,
            "unsupported_skills": unsupported
        }

    }