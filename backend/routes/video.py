import os

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from flask_jwt_extended import jwt_required, get_jwt_identity

from ai.video_processor import process_video
from services.history_service import HistoryService

video = Blueprint("video", __name__)

UPLOAD_FOLDER = "uploads/videos"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@video.route("/upload", methods=["POST"])
@jwt_required()
def upload_video():

    if "video" not in request.files:
        return jsonify({
            "success": False,
            "message": "Video file is required."
        }), 400

    file = request.files["video"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    filename = secure_filename(file.filename)

    video_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(video_path)

    try:

        result = process_video(video_path)

        transcript = result["transcript"]
        summary = result["summary"]

        user_id = get_jwt_identity()

        HistoryService.save_history(
            user_id=user_id,
            module="Video Summarizer",
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