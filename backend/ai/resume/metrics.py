import re


def has_date(section_text):
    """
    Detects common date formats.
    """

    patterns = [
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}",
        r"\b\d{2}/\d{4}\b",
        r"\b\d{4}\s*-\s*\d{4}\b",
        r"\b\d{4}\s*-\s*Present\b",
        r"\bPresent\b",
    ]

    for pattern in patterns:
        if re.search(pattern, section_text, re.IGNORECASE):
            return True

    return False


def extract_section(text, section_names):
    """
    Returns text belonging to a section.
    """

    lines = text.split("\n")

    capture = False

    result = []

    for line in lines:

        lower = line.lower().strip()

        if any(name in lower for name in section_names):
            capture = True
            continue

        if capture:

            if lower == "":
                break

            result.append(line)

    return "\n".join(result)


def calculate_metrics(resume_text):

    lines = [
        line.strip()
        for line in resume_text.split("\n")
        if line.strip()
    ]

    words = resume_text.split()

    bullets = [
        line
        for line in lines
        if line.startswith(("•", "-", "*"))
    ]

    # ---------------- Contact ----------------

    email = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            resume_text,
        )
    )

    phone = bool(
        re.search(
            r"\+?\d[\d\s\-]{8,}\d",
            resume_text,
        )
    )

    linkedin = "linkedin.com" in resume_text.lower()

    github = "github.com" in resume_text.lower()

    # ---------------- Sections ----------------

    education = extract_section(
        resume_text,
        ["education"]
    )

    experience = extract_section(
        resume_text,
        [
            "experience",
            "internship",
            "work experience"
        ]
    )

    projects = extract_section(
        resume_text,
        [
            "projects",
            "project"
        ]
    )

    certifications = extract_section(
        resume_text,
        [
            "certification",
            "certifications"
        ]
    )

    # ---------------- Metrics ----------------

    metrics = {

        "Characters": len(resume_text),

        "Words": len(words),

        "Lines": len(lines),

        "Pages": max(
            1,
            round(len(words) / 500)
        ),

        "Bullet Points": len(bullets),

        "Average Bullet Length":
        round(
            sum(len(x.split()) for x in bullets)
            / max(len(bullets), 1),
            1
        ),

        "Email": email,

        "Phone": phone,

        "LinkedIn": linkedin,

        "GitHub": github,

        "Education Date":
        has_date(education),

        "Experience Date":
        has_date(experience),

        "Project Date":
        has_date(projects),

        "Certification Date":
        has_date(certifications),

        "Project Count":
        resume_text.lower().count("project"),

        "Experience Count":
        resume_text.lower().count("intern")
        + resume_text.lower().count("experience"),

        "Blank Lines":
        resume_text.count("\n\n")

    }

    return metrics