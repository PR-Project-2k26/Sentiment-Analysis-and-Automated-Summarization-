def detect_sections(resume_text):

    text = resume_text.lower()

    section_keywords = {

        "Contact Information": [
            "email",
            "phone",
            "linkedin",
            "github"
        ],

        "Summary": [
            "summary",
            "profile",
            "objective",
            "about"
        ],

        "Education": [
            "education",
            "college",
            "university",
            "b.tech",
            "bachelor",
            "cgpa"
        ],

        "Skills": [
            "skills",
            "technical skills",
            "technologies"
        ],

        "Projects": [
            "projects",
            "project"
        ],

        "Experience": [
            "experience",
            "internship",
            "work experience"
        ],

        "Certifications": [
            "certification",
            "certifications",
            "certificate"
        ],

        "Achievements": [
            "achievement",
            "achievements",
            "award",
            "awards",
            "honors"
        ],

        "Leadership": [
            "leadership",
            "positions of responsibility",
            "responsibility"
        ],

        "Volunteer": [
            "volunteer",
            "volunteering",
            "community service"
        ],

        "Publications": [
            "publication",
            "publications",
            "research paper"
        ],

        "Languages": [
            "languages"
        ],

        "Coursework": [
            "coursework",
            "relevant coursework"
        ]
    }

    results = {}

    for section, keywords in section_keywords.items():

        results[section] = any(
            keyword in text
            for keyword in keywords
        )

    return results