"""
=========================================================
AI Career Intelligence Platform
Report Controller
=========================================================
"""

from flask import jsonify, request, g
from services.report_service import ReportService
from utils.decorators import login_required


class ReportController:
    """
    Report Controller handling candidate intelligence report generation & export.
    """

    @staticmethod
    def get_user_reports():
        user_id = getattr(g, "user_id", 1)
        reports = ReportService.get_user_reports(user_id)
        return jsonify({
            "success": True,
            "reports": reports
        }), 200

    @staticmethod
    def generate_report():
        data = request.get_json(silent=True) or {}
        user_id = getattr(g, "user_id", 1)
        resume_id = data.get("resume_id")
        
        result = ReportService.generate_report(user_id=user_id, resume_id=resume_id)
        return jsonify(result), 200
