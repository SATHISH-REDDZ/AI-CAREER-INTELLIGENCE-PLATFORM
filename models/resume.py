"""
=========================================================
AI Career Intelligence Platform
Resume Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Resume(BaseModel):
    """
    Resume Model
    """

    __tablename__ = "resumes"

    # -----------------------------------------------------
    # Resume Owner
    # -----------------------------------------------------

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # -----------------------------------------------------
    # File Information
    # -----------------------------------------------------

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    file_path = db.Column(
        db.String(500),
        nullable=False
    )

    file_type = db.Column(
        db.String(20),
        nullable=False
    )

    file_size = db.Column(
        db.Integer,
        nullable=False
    )

    # -----------------------------------------------------
    # AI Analysis
    # -----------------------------------------------------

    extracted_text = db.Column(
        db.Text,
        nullable=True
    )

    resume_score = db.Column(
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

    missing_skills = db.Column(
        db.Text,
        nullable=True
    )

    ai_summary = db.Column(
        db.Text,
        nullable=True
    )

    recommended_role = db.Column(
        db.String(150),
        nullable=True
    )

    # -----------------------------------------------------
    # Resume Status
    # -----------------------------------------------------

    status = db.Column(
        db.String(50),
        default="Uploaded"
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "file_type": self.file_type,
            "file_size": self.file_size,
            "resume_score": self.resume_score,
            "ats_score": self.ats_score,
            "skill_match": self.skill_match,
            "missing_skills": self.missing_skills,
            "recommended_role": self.recommended_role,
            "status": self.status,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    # -----------------------------------------------------
    # String Representation
    # -----------------------------------------------------

    def __repr__(self):
        return (
            f"<Resume "
            f"id={self.id} "
            f"file='{self.file_name}' "
            f"user_id={self.user_id}>"
        )