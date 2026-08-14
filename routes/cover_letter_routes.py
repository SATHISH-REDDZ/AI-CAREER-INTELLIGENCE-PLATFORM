"""
=========================================================
AI Career Intelligence Platform
Cover Letter Routes
=========================================================
"""

from flask import Blueprint
from controllers.cover_letter_controller import CoverLetterController
from utils.decorators import login_required

cover_letter_bp = Blueprint(
    "cover_letter",
    __name__,
    url_prefix="/api/cover-letter"
)


@cover_letter_bp.route("/generate", methods=["POST"])
@login_required
def generate_cover_letter():
    return CoverLetterController.generate_cover_letter()
