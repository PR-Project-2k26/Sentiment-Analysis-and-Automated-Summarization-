def calculate_resume_score(

    ats_score,

    job_match,

    metrics,

    sections,

    content_quality

):

    breakdown = {}

    # --------------------------------------------------
    # ATS Compatibility (20)
    # --------------------------------------------------

    breakdown["ATS Compatibility"] = ats_score

    # --------------------------------------------------
    # Job Match (40)
    # --------------------------------------------------

    breakdown["Job Match"] = job_match["score"]

    # --------------------------------------------------
    # Content Quality (20)
    # --------------------------------------------------

    content = 0

    content += round(content_quality["Grammar"] / 10 * 2)

    content += round(content_quality["Professional Tone"] / 10 * 2)

    content += round(content_quality["Clarity"] / 10 * 2)

    content += round(content_quality["Readability"] / 10 * 2)

    content += round(content_quality["Conciseness"] / 10 * 2)

    content += round(content_quality["Achievement Impact"] / 10 * 3)

    content += round(content_quality["Bullet Quality"] / 10 * 2)

    content += round(content_quality["Verb Variety"] / 10 * 1)

    content += round(content_quality["Keyword Optimization"] / 10 * 2)

    content += round(content_quality["Project Quality"] / 10 * 2)

    content += round(content_quality["Resume Consistency"] / 10 * 1)

    content += round(content_quality["Quantification"] / 10 * 1)

    breakdown["Content Quality"] = min(content, 20)

    # --------------------------------------------------
    # Resume Structure (20)
    # --------------------------------------------------

    structure = 0

    # Essential Sections (8)

    essential = [

        "Education",

        "Skills",

        "Projects",

        "Experience"

    ]

    section_marks = 8 / len(essential)

    for sec in essential:

        if sections.get(sec):
            structure += section_marks

    # Certifications (2)

    if sections.get("Certifications"):
        structure += 2

    # Achievements (2)

    if sections.get("Achievements"):
        structure += 2

    # Resume Length (3)

    if 300 <= metrics["Words"] <= 700:
        structure += 3

    elif 250 <= metrics["Words"] <= 800:
        structure += 2

    elif metrics["Words"] >= 200:
        structure += 1

    # Bullet Points (2)

    if metrics["Bullet Points"] >= 8:
        structure += 2

    elif metrics["Bullet Points"] >= 4:
        structure += 1

    # Dates (3)

    if metrics["Education Date"]:
        structure += 0.75

    if metrics["Experience Date"]:
        structure += 0.75

    if metrics["Project Date"]:
        structure += 0.75

    if metrics["Certification Date"]:
        structure += 0.75

    breakdown["Resume Structure"] = round(min(structure, 20))

    # --------------------------------------------------

    total = sum(breakdown.values())

    return total, breakdown