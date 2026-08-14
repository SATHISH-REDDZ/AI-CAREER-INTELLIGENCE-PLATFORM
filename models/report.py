"""
=========================================================
AI Career Intelligence Platform
Report Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Report(BaseModel):
    """
    AI Resume Analysis Report
    """

    __tablename__ = "reports"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    resume_id = db.Column(
        db.Integer,
        db.ForeignKey("resumes.id"),
        nullable=False
    )

    report_name = db.Column(
        db.String(200),
        nullable=False
    )

    overall_score = db.Column(
        db.Float,
        default=0.0
    )

    ats_score = db.Column(
        db.Float,
        default=0.0
    )

    skill_match = db.Column(
        db.Float,
        default=0.0
    )

    strengths = db.Column(
        db.Text
    )

    weaknesses = db.Column(
        db.Text
    )

    recommendations = db.Column(
        db.Text
    )

    generated_by = db.Column(
        db.String(100),
        default="AI Career Intelligence Platform"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "report_name": self.report_name,
            "overall_score": self.overall_score,
            "ats_score": self.ats_score,
            "skill_match": self.skill_match
        }