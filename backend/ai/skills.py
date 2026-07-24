import re

# Master list of skills
SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "html",
    "css",
    "react",
    "node",
    "express",
    "django",
    "flask",
    "fastapi",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "power bi",
    "excel",
    "data analysis",
    "data structures",
    "algorithms",
    "oop",
    "linux"
}

def extract_skills(text):
    text = text.lower()

    found = set()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.add(skill)

    return found



def calculate_skill_match(resume_skills, jd_skills):

    matched = resume_skills.intersection(jd_skills)

    missing = jd_skills - resume_skills

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_skills)) * 40)

    return score, matched, missing