"""
=========================================================
AI Career Intelligence Platform
Roadmap Controller
=========================================================
"""

from flask import jsonify, request, g
from services.roadmap_service import RoadmapService


class RoadmapController:
    """
    Career Roadmap Controller
    """

    @staticmethod
    def get_roadmap():
        data = request.args
        target_role = data.get("target_role", "Python Developer")
        result = RoadmapService.get_roadmap_for_role(target_role)
        return jsonify(result), 200
