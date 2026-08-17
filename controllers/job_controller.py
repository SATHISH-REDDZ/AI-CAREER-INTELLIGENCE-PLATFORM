"""
=========================================================
AI Career Intelligence Platform
Job Controller
=========================================================
"""

from flask import jsonify, request, g
from models.job import Job
from services.job_service import JobService
from utils.decorators import login_required


class JobController:
    """
    Job Controller handling job listing & recommendations.
    """

    @staticmethod
    def get_all_jobs():
        jobs = Job.query.filter_by(is_active=True).all()
        return jsonify({
            "success": True,
            "jobs": [j.to_dict() for j in jobs]
        }), 200

    @staticmethod
    def get_job_by_id(job_id: int):
        job = Job.query.get(job_id)
        if not job:
            return jsonify({
                "success": False,
                "message": "Job not found."
            }), 404
        return jsonify({
            "success": True,
            "job": job.to_dict()
        }), 200

    @staticmethod
    def get_job_recommendations():
        user_skills = request.args.getlist("skills")
        if not user_skills:
            user_skills = ["Python", "Flask", "SQL", "Git", "Docker"]
        
        recommendations = JobService.get_recommendations(user_skills)
        return jsonify({
            "success": True,
            "recommendations": recommendations
        }), 200
