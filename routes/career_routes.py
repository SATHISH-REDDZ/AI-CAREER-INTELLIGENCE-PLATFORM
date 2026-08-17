"""
=========================================================
AI Career Intelligence Platform
Career Routes
=========================================================
"""

from flask import Blueprint
from controllers.career_controller import CareerController

career_bp = Blueprint(
    "career",
    __name__,
    url_prefix="/api/career"
)


@career_bp.route("/recommend", methods=["POST", "GET"])
def recommend_career():
    return CareerController.recommend_career()


@career_bp.route("/skill-gap", methods=["POST", "GET"])
def skill_gap_analysis():
    return CareerController.skill_gap_analysis()
