"""
=========================================================
AI Career Intelligence Platform
Skill Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Skill(BaseModel):
    """
    Skill Model
    """

    __tablename__ = "skills"

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    demand_level = db.Column(
        db.String(50),
        default="Medium"
    )

    learning_resource = db.Column(
        db.String(500),
        nullable=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "demand_level": self.demand_level,
            "learning_resource": self.learning_resource
        }