from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.dashboard_service import DashboardService

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/stats", methods=["GET"])
@jwt_required()
def get_dashboard_stats():
    try:
        user_id = get_jwt_identity()

        stats = DashboardService.get_dashboard_stats(user_id)

        return jsonify(stats), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500