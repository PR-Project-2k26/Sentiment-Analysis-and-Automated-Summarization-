from ai.resume.parser import extract_resume_text
from ai.resume.metrics import calculate_metrics
from ai.resume.sections import detect_sections
from ai.resume.content_quality import evaluate_content_quality
from ai.resume.ats import calculate_ats
from ai.resume.skills import analyze_job_match
from ai.resume.score import calculate_resume_score
from ai.resume.suggestions import generate_suggestions
from ai.resume.ai_analyzer import analyze_resume_ai
from ai.resume.career_roadmap import generate_career_roadmap


def process_resume(pdf_path, job_description):

    # Extract resume text
    resume_text = extract_resume_text(pdf_path)

    # Calculate metrics
    metrics = calculate_metrics(resume_text)

    # Detect resume sections
    sections = detect_sections(resume_text)

    # AI content quality
    content_quality = evaluate_content_quality(
        resume_text,
        metrics
    )

    # ATS score
    ats_score, ats_report = calculate_ats(
        metrics,
        sections
    )

    # Job match
    job_match = analyze_job_match(
        resume_text,
        job_description
    )

    # Matched & Missing skills
    matched = (
        job_match["technical"]["matched"]
        + job_match["frameworks"]["matched"]
    )

    missing = (
        job_match["technical"]["missing"]
        + job_match["frameworks"]["missing"]
    )

    # Overall Resume Score
    resume_score, score_breakdown = calculate_resume_score(
        ats_score,
        job_match,
        metrics,
        sections,
        content_quality
    )

    # Suggestions
    suggestions = generate_suggestions(
        metrics,
        sections,
        missing,
        job_match,
        ats_report,
        content_quality
    )

    # AI Review
    ai_review = analyze_resume_ai(
        resume_text,
        job_description
    )

    # Career Roadmap
    career_roadmap = generate_career_roadmap(
        resume_text,
        job_description,
        missing
    )

    return {

        "resume_text": resume_text,

        "resume_score": resume_score,

        "ats_score": ats_score,

        "job_match": job_match,

        "metrics": metrics,

        "sections": sections,

        "content_quality": content_quality,

        "ats_report": ats_report,

        "matched_skills": matched,

        "missing_skills": missing,

        "score_breakdown": score_breakdown,

        "suggestions": suggestions,

        "ai_review": ai_review,

        "career_roadmap": career_roadmap

    }