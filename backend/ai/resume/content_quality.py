from ai.resume.ai_content import evaluate_ai_content


def evaluate_content_quality(resume_text, metrics):
    """
    Uses AI-generated writing quality scores.
    Returns scores out of 10 for each category.
    """

    ai = evaluate_ai_content(resume_text)

    report = {
        "Grammar": ai["grammar"]["score"],
        "Professional Tone": ai["professional_tone"]["score"],
        "Clarity": ai["clarity"]["score"],
        "Readability": ai["readability"]["score"],
        "Conciseness": ai["conciseness"]["score"],
        "Achievement Impact": ai["achievement_impact"]["score"],
        "Bullet Quality": ai["bullet_quality"]["score"],
        "Verb Variety": ai["verb_variety"]["score"],
        "Keyword Optimization": ai["keyword_optimization"]["score"],
        "Project Quality": ai["project_quality"]["score"],
        "Resume Consistency": ai["resume_consistency"]["score"],
        "Quantification": ai["quantification"]["score"],
        "ATS Friendly Writing": ai["ats_writing"]["score"],
        "Overall": round(
            (
                ai["grammar"]["score"]
                + ai["professional_tone"]["score"]
                + ai["clarity"]["score"]
                + ai["readability"]["score"]
                + ai["conciseness"]["score"]
                + ai["achievement_impact"]["score"]
                + ai["bullet_quality"]["score"]
                + ai["verb_variety"]["score"]
                + ai["keyword_optimization"]["score"]
                + ai["project_quality"]["score"]
                + ai["resume_consistency"]["score"]
                + ai["quantification"]["score"]
                + ai["ats_writing"]["score"]
            ) / 13,
            1
        ),
        "Feedback": ai["feedback"]
    }

    return report