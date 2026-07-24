import os

from flask import Blueprint, request, jsonify

from werkzeug.utils import secure_filename

from ai.parser import extract_resume_text

resume = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads/resumes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@resume.route("/upload", methods=["POST"])
def upload_resume():

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

    filename = secure_filename(file.filename)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(file_path)

    resume_text = extract_resume_text(file_path)

    return jsonify({
        "success": True,
        "fileName": filename,
        "resumeText": resume_text
    }), 200