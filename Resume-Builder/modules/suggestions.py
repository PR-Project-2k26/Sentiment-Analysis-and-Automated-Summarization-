def generate_suggestions(resume_text, missing_skills):
    """
    Generate resume improvement suggestions.
    """

    suggestions = []

    resume = resume_text.lower()

    # Missing skills
    for skill in sorted(missing_skills):
        suggestions.append(f"Consider adding experience with {skill.title()}.")

    # GitHub
    if "github" not in resume:
        suggestions.append("Add your GitHub profile link.")

    # LinkedIn
    if "linkedin" not in resume:
        suggestions.append("Add your LinkedIn profile.")

    # Projects
    if "project" not in resume:
        suggestions.append("Include at least 2 strong technical projects.")

    # Certifications
    if "certification" not in resume and "certificate" not in resume:
        suggestions.append("Mention relevant certifications.")

    # Numbers
    has_number = any(ch.isdigit() for ch in resume)

    if not has_number:
        suggestions.append(
            "Quantify your achievements using numbers wherever possible."
        )

    return suggestions