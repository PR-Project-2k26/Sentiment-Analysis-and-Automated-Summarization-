from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.history_service import HistoryService

history = Blueprint("history", __name__)


# ----------------------------
# Save History
# ----------------------------
@history.route("/", methods=["POST"])
@jwt_required()
def save_history():

    data = request.get_json()

    module = data.get("module")
    file_name = data.get("file_name")
    summary = data.get("summary")
    processing_time = data.get("processing_time", 0)
    status = data.get("status", "Completed")

    if not module or not file_name or not summary:
        return jsonify({
            "success": False,
            "message": "Module, file name and summary are required."
        }), 400

    user_id = get_jwt_identity()

    history_id = HistoryService.save_history(
        user_id=user_id,
        module=module,
        file_name=file_name,
        summary=summary,
        processing_time=processing_time,
        status=status,
    )

    return jsonify({
        "success": True,
        "message": "History saved successfully.",
        "history_id": history_id
    }), 201