import re

def calculate_metrics(resume_text):
    lines = [line.strip() for line in resume_text.split("\n") if line.strip()]
    words = resume_text.split()

    metrics = {
        "Characters": len(resume_text),
        "Words": len(words),
        "Lines": len(lines),
        "Pages": max(1, round(len(words) / 500)),
        "Bullet Points": sum(
            line.startswith(("•", "-", "*"))
            for line in lines
        ),
        "Email": bool(
            re.search(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                resume_text
            )
        ),
        "Phone": bool(
            re.search(
                r"\+?\d[\d\s\-]{8,}\d",
                resume_text
            )
        ),
        "LinkedIn": "linkedin.com" in resume_text.lower(),
        "GitHub": "github.com" in resume_text.lower(),
    }

    return metrics