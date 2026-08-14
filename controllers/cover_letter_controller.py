"""
=========================================================
AI Career Intelligence Platform
Cover Letter Controller
=========================================================
"""

from flask import jsonify, request, g
from services.cover_letter_service import CoverLetterService


class CoverLetterController:
    """
    Cover Letter Controller
    """

    @staticmethod
    def generate_cover_letter():
        data = request.get_json(silent=True) or {}
        company_name = data.get("company_name", "TechInnovate Inc.")
        job_title = data.get("job_title", "Python Developer")
        job_description = data.get("job_description", "")

        result = CoverLetterService.generate_cover_letter(
            user_id=g.user_id,
            company_name=company_name,
            job_title=job_title,
            job_description=job_description
        )
        return jsonify(result), 200
