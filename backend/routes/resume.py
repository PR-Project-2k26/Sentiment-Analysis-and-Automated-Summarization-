import os

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from flask_jwt_extended import jwt_required, get_jwt_identity

from ai.resume_processor import process_resume
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
    # Job Description
    # -----------------------------
    job_description = request.form.get(
        "jobDescription",
        ""
    )

    try:

        # -----------------------------
        # AI Resume Processing
        # -----------------------------
        result = process_resume(
            file_path,
            job_description
        )

        # -----------------------------
        # Save History
        # -----------------------------
        user_id = get_jwt_identity()

        summary = (
            f"Resume Score: {result['resume_score']}/100 | "
            f"ATS: {result['ats_score']}/20 | "
            f"Job Match: {result['job_match']['score']}/40"
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

            "resumeScore": result["resume_score"],

            "atsScore": result["ats_score"],

            "jobMatch": result["job_match"],

            "metrics": result["metrics"],

            "sections": result["sections"],

            "contentQuality": result["content_quality"],

            "scoreBreakdown": result["score_breakdown"],

            "matchedSkills": result["matched_skills"],

            "missingSkills": result["missing_skills"],

            "atsReport": result["ats_report"],

            "suggestions": result["suggestions"],

            "aiReview": result["ai_review"],

            "careerRoadmap": result["career_roadmap"]

        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500