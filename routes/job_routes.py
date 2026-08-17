"""
=========================================================
AI Career Intelligence Platform
Job Routes
=========================================================
"""

from flask import Blueprint
from controllers.job_controller import JobController
from utils.decorators import login_required

job_bp = Blueprint(
    "jobs",
    __name__,
    url_prefix="/api/jobs"
)


@job_bp.route("", methods=["GET"])
def get_all_jobs():
    return JobController.get_all_jobs()


@job_bp.route("/<int:job_id>", methods=["GET"])
def get_job_by_id(job_id):
    return JobController.get_job_by_id(job_id)


@job_bp.route("/recommendations", methods=["GET", "POST"])
def get_job_recommendations():
    return JobController.get_job_recommendations()
