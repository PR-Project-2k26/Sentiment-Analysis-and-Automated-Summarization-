import re

def calculate_ats(metrics, sections):

    score = 0

    strengths = []
    improvements = []

    # -----------------------------
    # Contact Information (4)
    # -----------------------------

    if metrics["Email"]:
        score += 1
        strengths.append("Professional email detected.")
    else:
        improvements.append("Add an email address.")

    if metrics["Phone"]:
        score += 1
        strengths.append("Phone number detected.")
    else:
        improvements.append("Add a phone number.")

    if metrics["LinkedIn"]:
        score += 1
        strengths.append("LinkedIn profile included.")
    else:
        improvements.append("Add your LinkedIn profile.")

    if metrics["GitHub"]:
        score += 1
        strengths.append("GitHub profile included.")
    else:
        improvements.append("Add your GitHub profile.")

    # -----------------------------
    # Essential Sections (4)
    # -----------------------------

    essential = [
        "Education",
        "Skills",
        "Projects",
        "Experience"
    ]

    section_marks = 4 / len(essential)

    for sec in essential:

        if sections.get(sec):

            score += section_marks
            strengths.append(f"{sec} section found.")

        else:

            improvements.append(
                f"Add a {sec} section."
            )

    # -----------------------------
    # ATS Formatting (4)
    # -----------------------------

    formatting = 0

    if 250 <= metrics["Words"] <= 800:
        formatting += 1
    else:
        improvements.append(
            "Keep resume between 250 and 800 words."
        )

    if metrics["Bullet Points"] >= 4:
        formatting += 1
    else:
        improvements.append(
            "Use bullet points for better readability."
        )

    if metrics["Lines"] >= 20:
        formatting += 1

    if metrics["Characters"] > 500:
        formatting += 1

    score += formatting

    if formatting == 4:
        strengths.append(
            "Resume formatting is ATS friendly."
        )

    # -----------------------------
    # Dates (2)
    # -----------------------------

    date_score = 0

    if metrics["Education Date"]:
        date_score += 0.5

    if metrics["Experience Date"]:
        date_score += 0.5

    if metrics["Project Date"]:
        date_score += 0.5

    if metrics["Certification Date"]:
        date_score += 0.5

    if date_score == 2:
        strengths.append(
            "Timeline is complete."
        )
    else:
        improvements.append(
            "Add dates to education, experience, projects and certifications."
        )

    score += date_score

    # -----------------------------
    # ATS Parseability (6)
    # -----------------------------

    parseability = 6

    if not metrics["Email"]:
        parseability -= 1

    if not metrics["Phone"]:
        parseability -= 1

    if metrics["Bullet Points"] == 0:
        parseability -= 1

    if metrics["Words"] < 150:
        parseability -= 2

    parseability = max(parseability,0)

    score += parseability

    if parseability == 6:
        strengths.append(
            "Resume is highly ATS parseable."
        )

    report = {

        "strengths": strengths,

        "improvements": improvements

    }

    return round(score), report