"""
=========================================================
AI Career Intelligence Platform
Resume Routes
=========================================================
"""

from flask import Blueprint

from controllers.resume_controller import ResumeController
from utils.decorators import login_required


resume_bp = Blueprint(
    "resume",
    __name__,
    url_prefix="/api/resumes"
)


@resume_bp.route("/upload", methods=["POST"])
@login_required
def upload_resume():
    return ResumeController.upload_resume()


@resume_bp.route("", methods=["GET"])
@login_required
def get_user_resumes():
    return ResumeController.get_user_resumes()


@resume_bp.route("/<int:resume_id>", methods=["GET"])
@login_required
def get_resume(resume_id):
    return ResumeController.get_resume(resume_id)


@resume_bp.route("/<int:resume_id>/analyze", methods=["POST"])
@login_required
def analyze_resume(resume_id):
    return ResumeController.analyze_resume(resume_id)


@resume_bp.route("/<int:resume_id>", methods=["DELETE"])
@login_required
def delete_resume(resume_id):
    return ResumeController.delete_resume(resume_id)