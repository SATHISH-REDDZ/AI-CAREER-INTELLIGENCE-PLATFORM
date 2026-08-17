"""
=========================================================
AI Career Intelligence Platform
Report Routes
=========================================================
"""

from flask import Blueprint
from controllers.report_controller import ReportController
from utils.decorators import login_required

report_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/reports"
)


@report_bp.route("", methods=["GET"])
@login_required
def get_user_reports():
    return ReportController.get_user_reports()


@report_bp.route("/generate", methods=["POST"])
@login_required
def generate_report():
    return ReportController.generate_report()
