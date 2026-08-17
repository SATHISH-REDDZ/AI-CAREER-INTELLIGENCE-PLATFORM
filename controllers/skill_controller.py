"""
=========================================================
AI Career Intelligence Platform
Skill Controller
=========================================================
"""

from flask import jsonify, request
from models.skill import Skill


class SkillController:
    """
    Skill Controller handling skill catalog APIs.
    """

    @staticmethod
    def get_all_skills():
        category = request.args.get("category")
        query = Skill.query
        if category:
            query = query.filter_by(category=category)
        skills = query.all()
        return jsonify({
            "success": True,
            "skills": [s.to_dict() for s in skills]
        }), 200

    @staticmethod
    def get_skill_by_id(skill_id: int):
        skill = Skill.query.get(skill_id)
        if not skill:
            return jsonify({
                "success": False,
                "message": "Skill not found."
            }), 404
        return jsonify({
            "success": True,
            "skill": skill.to_dict()
        }), 200
