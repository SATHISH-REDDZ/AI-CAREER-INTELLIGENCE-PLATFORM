"""
=========================================================
AI Career Intelligence Platform
Career Controller
=========================================================
"""

from flask import jsonify, request, g
from ml.career_prediction import CareerPredictionEngine
from ml.skill_gap import SkillGapAnalyzer


class CareerController:
    """
    Career Controller for ML career recommendations and skill gap analysis.
    """

    @staticmethod
    def recommend_career():
        data = request.get_json(silent=True) or {}
        skills = data.get("skills", ["Python", "Flask", "SQL", "Git"])
        
        predictions = CareerPredictionEngine.recommend_roles(skills)
        return jsonify({
            "success": True,
            "predictions": predictions
        }), 200

    @staticmethod
    def skill_gap_analysis():
        data = request.get_json(silent=True) or {}
        user_skills = data.get("skills", ["Python", "Flask", "SQL", "Git"])
        target_role = data.get("target_role", "Python Backend Developer")
        
        analysis = SkillGapAnalyzer.analyze(user_skills=user_skills, target_role=target_role)
        return jsonify({
            "success": True,
            "skill_gap_analysis": analysis
        }), 200
