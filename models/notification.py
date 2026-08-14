"""
=========================================================
AI Career Intelligence Platform
Notification Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Notification(BaseModel):
    """
    User Notification Model
    """

    __tablename__ = "notifications"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    notification_type = db.Column(
        db.String(100),
        default="General"
    )

    priority = db.Column(
        db.String(50),
        default="Normal"
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    action_url = db.Column(
        db.String(300),
        nullable=True
    )

    expires_at = db.Column(
        db.DateTime,
        nullable=True
    )

    def mark_as_read(self):
        """
        Mark notification as read.
        """
        self.is_read = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "notification_type": self.notification_type,
            "priority": self.priority,
            "is_read": self.is_read
        }

    def __repr__(self):
        return f"<Notification {self.id}>"