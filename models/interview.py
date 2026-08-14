"""
=========================================================
AI Career Intelligence Platform
Interview Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Interview(BaseModel):
    """
    AI Mock Interview
    """

    __tablename__ = "interviews"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    interview_type = db.Column(
        db.String(100),
        nullable=False
    )

    difficulty = db.Column(
        db.String(50),
        default="Medium"
    )

    score = db.Column(
        db.Float,
        default=0.0
    )

    total_questions = db.Column(
        db.Integer,
        default=0
    )

    answered_questions = db.Column(
        db.Integer,
        default=0
    )

    feedback = db.Column(
        db.Text
    )

    ai_recommendation = db.Column(
        db.Text
    )

    duration = db.Column(
        db.Integer,
        default=0
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "interview_type": self.interview_type,
            "difficulty": self.difficulty,
            "score": self.score,
            "completed": self.completed
        }