"""
=========================================================
AI Career Intelligence Platform
Resume Controller
=========================================================
"""

from flask import jsonify, request, g

from repositories.resume_repository import ResumeRepository
from services.resume_service import ResumeService


class ResumeController:
    """
    Resume Controller
    """

    @staticmethod
    def upload_resume():
        """
        Upload Resume
        """
        if "file" not in request.files:
            return jsonify({
                "success": False,
                "message": "Resume file is required."
            }), 400

        file = request.files["file"]

        user_id = getattr(g, "user_id", 1) or 1

        success, result = ResumeService.upload_resume(
            user_id=user_id,
            file=file
        )

        if success:
            return jsonify({
                "success": True,
                "message": "Resume uploaded successfully.",
                "resume": result.to_dict()
            }), 201

        return jsonify({
            "success": False,
            "message": result
        }), 400

    @staticmethod
    def get_user_resumes():
        """
        Get all resumes for logged in user.
        """
        resumes = ResumeRepository.get_by_user(g.user_id)
        return jsonify({
            "success": True,
            "resumes": [r.to_dict() for r in resumes]
        }), 200

    @staticmethod
    def get_resume(resume_id: int):
        """
        Get specific resume by ID.
        """
        resume = ResumeRepository.get_by_id(resume_id)
        if not resume or resume.user_id != g.user_id:
            return jsonify({
                "success": False,
                "message": "Resume not found."
            }), 404

        return jsonify({
            "success": True,
            "resume": resume.to_dict()
        }), 200

    @staticmethod
    def analyze_resume(resume_id: int):
        """
        Trigger AI analysis on uploaded resume.
        """
        resume = ResumeRepository.get_by_id(resume_id)
        if not resume or resume.user_id != g.user_id:
            return jsonify({
                "success": False,
                "message": "Resume not found."
            }), 404

        data = request.get_json(silent=True) or {}
        target_role = data.get("target_role", "Python Developer")

        success, result = ResumeService.analyze_resume(resume_id, target_role=target_role)

        if success:
            return jsonify({
                "success": True,
                "message": "Resume analysis completed successfully.",
                "resume": result.to_dict()
            }), 200

        return jsonify({
            "success": False,
            "message": result
        }), 400

    @staticmethod
    def delete_resume(resume_id: int):
        """
        Delete a resume.
        """
        resume = ResumeRepository.get_by_id(resume_id)
        if not resume or resume.user_id != g.user_id:
            return jsonify({
                "success": False,
                "message": "Resume not found."
            }), 404

        ResumeRepository.delete(resume)
        return jsonify({
            "success": True,
            "message": "Resume deleted successfully."
        }), 200