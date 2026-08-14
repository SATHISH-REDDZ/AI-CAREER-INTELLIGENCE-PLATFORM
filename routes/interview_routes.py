"""
=========================================================
AI Career Intelligence Platform
Interview Routes
=========================================================
"""

from flask import Blueprint
from controllers.interview_controller import InterviewController
from utils.decorators import login_required

interview_bp = Blueprint(
    "interview",
    __name__,
    url_prefix="/api/interview"
)


@interview_bp.route("/generate-questions", methods=["POST"])
@login_required
def generate_questions():
    return InterviewController.generate_questions()


@interview_bp.route("/submit-answer", methods=["POST"])
@login_required
def evaluate_answer():
    return InterviewController.evaluate_answer()
