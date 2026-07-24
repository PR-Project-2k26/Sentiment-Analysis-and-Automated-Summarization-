from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ai.text_processor import summarize_text
from services.history_service import HistoryService

text = Blueprint("text", __name__)


@text.route("/summarize", methods=["POST"])
@jwt_required()
def summarize():

    data = request.get_json()

    input_text = data.get("text", "").strip()
    length = data.get("length", "Medium")

    if not input_text:
        return jsonify({
            "success": False,
            "message": "Text is required."
        }), 400

    try:
        result = summarize_text(input_text, length)

        user_id = get_jwt_identity()

        HistoryService.save_history(
            user_id=user_id,
            module="Text Summarizer",
            file_name="Manual Text",
            summary=result["summary"][:250] + "..." if len(result["summary"]) > 250 else result["summary"],
            processing_time=result["latency_sec"],
            status="Completed"
        )

        return jsonify({
            "success": True,
            **result
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500