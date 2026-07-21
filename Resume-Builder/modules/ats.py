def calculate_ats(metrics, sections):
    """
    Returns:
        score (out of 20)
        report (strengths & improvements)
    """

    score = 0

    strengths = []
    improvements = []

    # ---------------- Contact Information (6) ----------------

    if metrics["Email"]:
        score += 2
        strengths.append("📧 Email address found")
    else:
        improvements.append("Add a professional email address")

    if metrics["Phone"]:
        score += 2
        strengths.append("📱 Phone number found")
    else:
        improvements.append("Add your phone number")

    if metrics["LinkedIn"]:
        score += 1
        strengths.append("💼 LinkedIn profile included")
    else:
        improvements.append("Add your LinkedIn profile")

    if metrics["GitHub"]:
        score += 1
        strengths.append("🐙 GitHub profile included")
    else:
        improvements.append("Add your GitHub profile")

    # ---------------- Resume Sections (10) ----------------

    total_sections = len(sections)
    present_sections = sum(sections.values())

    score += round((present_sections / total_sections) * 10)

    for section, present in sections.items():

        if present:
            strengths.append(f"✅ {section} section found")
        else:
            improvements.append(f"Add {section} section")

    # ---------------- Resume Length (4) ----------------

    words = metrics["Words"]

    if 250 <= words <= 800:

        score += 4
        strengths.append("📄 Resume length is ATS-friendly")

    elif words >= 150:

        score += 2
        improvements.append("Resume could be slightly longer (250–800 words recommended)")

    else:

        improvements.append("Resume is too short")

    report = {
        "strengths": strengths,
        "improvements": improvements
    }

    return score, report