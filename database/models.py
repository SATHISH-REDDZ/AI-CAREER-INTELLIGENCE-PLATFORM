"""
=========================================================
AI Career Intelligence Platform
Base Database Models
=========================================================

This module defines the abstract base model that all
database models inherit from.
=========================================================
"""

from datetime import datetime, timezone

from app.extensions import db


class BaseModel(db.Model):
    """
    Abstract base model containing common fields.
    """

    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    def save(self):
        """
        Save the current object.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current object.
        """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"