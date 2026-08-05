def generate_suggestions(
    metrics,
    sections,
    missing_skills,
    job_match,
    ats_report,
    content_quality
):
    """
    Generates prioritized resume improvement suggestions.
    """

    suggestions = {
        "High Priority": [],
        "Medium Priority": [],
        "Low Priority": []
    }

    # ---------------------------------
    # Missing Technical Skills
    # ---------------------------------

    for skill in sorted(missing_skills):
        suggestions["High Priority"].append(
            f"Add **{skill}** if you have experience with it. It is required by the Job Description."
        )

    # ---------------------------------
    # ATS Improvements
    # ---------------------------------

    for item in ats_report["improvements"]:
        suggestions["High Priority"].append(item)

    # ---------------------------------
    # Unsupported Skills
    # ---------------------------------

    unsupported = job_match["evidence"]["unsupported_skills"]

    if unsupported:

        suggestions["High Priority"].append(

            "Demonstrate these skills inside Projects or Experience instead of only listing them: "

            + ", ".join(unsupported)

        )

    # ---------------------------------
    # Weak Project Description
    # ---------------------------------

    if job_match["projects"]["quality"] in ["Poor", "Average"]:

        suggestions["High Priority"].append(

            "Improve project descriptions by mentioning technologies used, technical challenges, and measurable outcomes."

        )

    # ---------------------------------
    # Weak Experience
    # ---------------------------------

    if job_match["experience"]["quality"] == "Poor":

        suggestions["Medium Priority"].append(

            "Add internships, freelance work, open-source contributions, or hackathon experience."

        )

    # ---------------------------------
    # Weak Action Words
    # ---------------------------------

    weak = job_match["action"]["weak"]

    if weak:

        suggestions["Medium Priority"].append(

            "Replace weak action words such as "

            + ", ".join(weak)

            + " with stronger verbs like Developed, Implemented, Designed, Optimized."

        )

    # ---------------------------------
    # Missing Sections
    # ---------------------------------

    important = [

        "Projects",

        "Experience",

        "Skills",

        "Education"

    ]

    for sec in important:

        if not sections.get(sec):

            suggestions["High Priority"].append(

                f"Add a **{sec}** section."

            )

    # ---------------------------------
    # Certifications
    # ---------------------------------

    if not sections.get("Certifications"):

        suggestions["Low Priority"].append(

            "Include relevant certifications if available."

        )

    # ---------------------------------
    # Achievements
    # ---------------------------------

    if not sections.get("Achievements"):

        suggestions["Low Priority"].append(

            "Consider adding an Achievements section."

        )

    # ---------------------------------
    # AI Writing Feedback
    # ---------------------------------

    for item in content_quality["Feedback"]:

        suggestions["Medium Priority"].append(item)

    return suggestions