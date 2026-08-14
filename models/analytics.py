"""
=========================================================
AI Career Intelligence Platform
Analytics Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Analytics(BaseModel):
    """
    Dashboard Analytics
    """

    __tablename__ = "analytics"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    resumes_uploaded = db.Column(
        db.Integer,
        default=0
    )

    reports_generated = db.Column(
        db.Integer,
        default=0
    )

    chatbot_questions = db.Column(
        db.Integer,
        default=0
    )

    interview_sessions = db.Column(
        db.Integer,
        default=0
    )

    average_resume_score = db.Column(
        db.Float,
        default=0.0
    )

    average_ats_score = db.Column(
        db.Float,
        default=0.0
    )

    total_job_matches = db.Column(
        db.Integer,
        default=0
    )

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "resumes_uploaded": self.resumes_uploaded,
            "reports_generated": self.reports_generated,
            "average_resume_score": self.average_resume_score,
            "average_ats_score": self.average_ats_score
        }