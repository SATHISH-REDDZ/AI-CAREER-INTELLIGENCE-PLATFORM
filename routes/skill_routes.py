"""
=========================================================
AI Career Intelligence Platform
Skill Routes
=========================================================
"""

from flask import Blueprint
from controllers.skill_controller import SkillController

skill_bp = Blueprint(
    "skills",
    __name__,
    url_prefix="/api/skills"
)


@skill_bp.route("", methods=["GET"])
def get_all_skills():
    return SkillController.get_all_skills()


@skill_bp.route("/<int:skill_id>", methods=["GET"])
def get_skill_by_id(skill_id):
    return SkillController.get_skill_by_id(skill_id)
