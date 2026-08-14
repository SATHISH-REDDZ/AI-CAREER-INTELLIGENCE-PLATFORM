"""
=========================================================
AI Career Intelligence Platform
Analytics Controller
=========================================================
"""

from flask import jsonify, g
from services.analytics_service import AnalyticsService


class AnalyticsController:
    """
    Analytics Controller
    """

    @staticmethod
    def get_dashboard():
        result = AnalyticsService.get_user_dashboard_analytics(g.user_id)
        return jsonify(result), 200
