import os

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from flask_jwt_extended import jwt_required, get_jwt_identity

from ai.parser import extract_resume_text
from ai.metrics import calculate_metrics
from ai.sections import detect_sections
from ai.skills import extract_skills, calculate_skill_match
from ai.ats import calculate_ats
from ai.score import calculate_resume_score
from ai.suggestions import generate_suggestions

from services.history_service import HistoryService

resume = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads/resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@resume.route("/upload", methods=["POST"])
@jwt_required()
def upload_resume():

    # -----------------------------
    # Validate File
    # -----------------------------
    if "resume" not in request.files:
        return jsonify({
            "success": False,
            "message": "Resume file is required."
        }), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    # -----------------------------
    # Save File
    # -----------------------------
    filename = secure_filename(file.filename)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(file_path)

    # -----------------------------
    # Extract Resume Text
    # -----------------------------
    resume_text = extract_resume_text(file_path)

    # -----------------------------
    # Metrics
    # -----------------------------
    metrics = calculate_metrics(resume_text)

    # -----------------------------
    # Sections
    # -----------------------------
    sections = detect_sections(resume_text)

    # -----------------------------
    # Resume Skills
    # -----------------------------
    resume_skills = extract_skills(resume_text)

    # -----------------------------
    # Job Description
    # -----------------------------
    job_description = request.form.get(
        "jobDescription",
        ""
    )

    jd_skills = extract_skills(job_description)

    # -----------------------------
    # Skill Match
    # -----------------------------
    skill_score, matched_skills, missing_skills = calculate_skill_match(
        resume_skills,
        jd_skills
    )

    # -----------------------------
    # ATS
    # -----------------------------
    ats_score, ats_report = calculate_ats(
        metrics,
        sections
    )

    # -----------------------------
    # Resume Score
    # -----------------------------
    resume_score, score_breakdown = calculate_resume_score(
        ats_score,
        skill_score,
        metrics,
        sections
    )

    # -----------------------------
    # Suggestions
    # -----------------------------
    suggestions = generate_suggestions(
        resume_text,
        missing_skills
    )

    # -----------------------------
    # Save History
    # -----------------------------
    user_id = get_jwt_identity()

    summary = (
        f"Resume Score: {resume_score}/100 | "
        f"ATS: {ats_score}/20 | "
        f"Skill Match: {skill_score}/40"
    )

    HistoryService.save_history(
        user_id=user_id,
        module="Resume Analyzer",
        file_name=filename,
        summary=summary,
        processing_time=0,
        status="Completed"
    )

    # -----------------------------
    # Response
    # -----------------------------
    return jsonify({
        "success": True,
        "fileName": filename,

        "resumeScore": resume_score,
        "atsScore": ats_score,
        "skillScore": skill_score,

        "metrics": metrics,
        "sections": sections,

        "scoreBreakdown": score_breakdown,

        "resumeSkills": sorted(list(resume_skills)),
        "matchedSkills": sorted(list(matched_skills)),
        "missingSkills": sorted(list(missing_skills)),

        "atsReport": ats_report,

        "suggestions": suggestions
    }), 200