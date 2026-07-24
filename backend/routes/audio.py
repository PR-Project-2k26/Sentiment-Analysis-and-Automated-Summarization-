import os

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from ai.audio_processor import process_audio
from services.history_service import HistoryService

audio = Blueprint("audio", __name__)

UPLOAD_FOLDER = "uploads/audio"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@audio.route("/upload", methods=["POST"])
@jwt_required()
def upload_audio():

    if "audio" not in request.files:
        return jsonify({
            "success": False,
            "message": "Audio file is required."
        }), 400

    file = request.files["audio"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    filename = secure_filename(file.filename)

    audio_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(audio_path)

    try:
        result = process_audio(audio_path)

        transcript = result["transcript"]
        summary = result["summary"]

        user_id = get_jwt_identity()

        HistoryService.save_history(
            user_id=user_id,
            module="Audio Summarizer",
            file_name=filename,
            summary=summary[:250] + "..." if len(summary) > 250 else summary,
            processing_time=0,
            status="Completed"
        )

        return jsonify({
            "success": True,
            "fileName": filename,
            "transcript": transcript,
            "summary": summary
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500