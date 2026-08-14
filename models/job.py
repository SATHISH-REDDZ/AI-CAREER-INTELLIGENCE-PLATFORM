"""
=========================================================
AI Career Intelligence Platform
Job Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Job(BaseModel):
    """
    Job Model
    """

    __tablename__ = "jobs"

    title = db.Column(
        db.String(150),
        nullable=False
    )

    company = db.Column(
        db.String(150),
        nullable=False
    )

    location = db.Column(
        db.String(150),
        nullable=True
    )

    employment_type = db.Column(
        db.String(100),
        nullable=True
    )

    experience_level = db.Column(
        db.String(100),
        nullable=True
    )

    salary = db.Column(
        db.String(100),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    required_skills = db.Column(
        db.Text,
        nullable=True
    )

    application_url = db.Column(
        db.String(500),
        nullable=True
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "salary": self.salary,
            "experience_level": self.experience_level,
            "is_active": self.is_active
        }