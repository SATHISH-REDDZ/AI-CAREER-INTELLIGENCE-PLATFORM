"""
=========================================================
AI Career Intelligence Platform
Analytics Routes
=========================================================
"""

from flask import Blueprint
from controllers.analytics_controller import AnalyticsController
from utils.decorators import login_required

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/api/analytics"
)


@analytics_bp.route("/dashboard", methods=["GET"])
@login_required
def get_dashboard():
    return AnalyticsController.get_dashboard()
