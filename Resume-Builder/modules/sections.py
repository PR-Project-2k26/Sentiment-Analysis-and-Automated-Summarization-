def detect_sections(resume_text):
    """
    Detect important resume sections.
    """

    text = resume_text.lower()

    section_keywords = {
        "Contact Information": [
            "email",
            "phone",
            "linkedin",
            "github"
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
            "technical skills"
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
            "certifications",
            "certificate"
        ],

        "Achievements": [
            "achievements",
            "awards",
            "honors"
        ],

        "Languages": [
            "languages"
        ],

    
    }

    results = {}

    for section, keywords in section_keywords.items():

        found = any(keyword in text for keyword in keywords)

        results[section] = found

    return results