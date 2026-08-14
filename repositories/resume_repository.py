"""
=========================================================
AI Career Intelligence Platform
Resume Repository
=========================================================
"""

from app.extensions import db
from models import resume
from models.resume import Resume


class ResumeRepository:
    """
    Resume Repository
    """

    @staticmethod
    def create(resume: Resume):
        """
        Create a new resume.
        """

        print("\n========== REPOSITORY ==========")

        print("Adding Resume")

        db.session.add(resume)

        print("Before Commit")

        db.session.commit()

        print("Commit Success")

        return resume

    @staticmethod
    def get_by_id(resume_id: int):
        """
        Get resume by ID.
        """
        return Resume.query.filter_by(
            id=resume_id,
            is_active=True
        ).first()

    @staticmethod
    def get_by_user(user_id: int):
        """
        Get all resumes for a user.
        """
        return Resume.query.filter_by(
            user_id=user_id,
            is_active=True
        ).order_by(
            Resume.created_at.desc()
        ).all()

    @staticmethod
    def update(resume: Resume):
        """
        Save resume changes.
        """
        db.session.commit()
        return resume

    @staticmethod
    def delete(resume: Resume):
        """
        Soft delete resume.
        """
        resume.is_active = False
        db.session.commit()

    @staticmethod
    def update_ai_analysis(
        resume: Resume,
        extracted_text=None,
        resume_score=None,
        ats_score=None,
        skill_match=None,
        missing_skills=None,
        ai_summary=None,
        recommended_role=None
    ):
        """
        Update AI analysis results.
        """

        if extracted_text is not None:
            resume.extracted_text = extracted_text

        if resume_score is not None:
            resume.resume_score = resume_score

        if ats_score is not None:
            resume.ats_score = ats_score

        if skill_match is not None:
            resume.skill_match = skill_match

        if missing_skills is not None:
            resume.missing_skills = missing_skills

        if ai_summary is not None:
            resume.ai_summary = ai_summary

        if recommended_role is not None:
            resume.recommended_role = recommended_role

        db.session.commit()

        return resume