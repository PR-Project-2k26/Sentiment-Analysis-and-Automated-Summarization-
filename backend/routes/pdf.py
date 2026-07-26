import time

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ai.pdf_processor import (
    extract_text_from_pdf,
    summarize_large_text
)

from services.history_service import HistoryService

pdf = Blueprint("pdf", __name__)


@pdf.route("/upload", methods=["POST"])
@jwt_required()
def upload_pdf():

    # -----------------------------
    # Validate File
    # -----------------------------
    if "pdf" not in request.files:
        return jsonify({
            "success": False,
            "message": "PDF file is required."
        }), 400

    file = request.files["pdf"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({
            "success": False,
            "message": "Only PDF files are allowed."
        }), 400

    try:

        start = time.time()

        # -----------------------------
        # Extract Text
        # -----------------------------
        text = extract_text_from_pdf(file)

        if not text.strip():
            return jsonify({
                "success": False,
                "message": "No readable text found in the uploaded PDF."
            }), 400

        # -----------------------------
        # Summarize
        # -----------------------------
        summary = summarize_large_text(text)

        processing_time = round(time.time() - start, 2)

        # -----------------------------
        # Save History
        # -----------------------------
        user_id = get_jwt_identity()

        HistoryService.save_history(
            user_id=user_id,
            module="PDF Summarizer",
            file_name=file.filename,
            summary=summary[:250] + "..." if len(summary) > 250 else summary,
            processing_time=processing_time,
            status="Completed"
        )

        # -----------------------------
        # Response
        # -----------------------------
        return jsonify({
            "success": True,
            "filename": file.filename,
            "characters": len(text),
            "summary": summary
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500