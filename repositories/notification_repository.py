"""
=========================================================
AI Career Intelligence Platform
Notification Repository
=========================================================
"""

from typing import List, Optional

from app.extensions import db
from models.notification import Notification


class NotificationRepository:
    """
    Repository for Notification model.
    """

    @staticmethod
    def create(notification: Notification) -> Notification:
        db.session.add(notification)
        db.session.commit()
        return notification

    @staticmethod
    def get_by_id(notification_id: int) -> Optional[Notification]:
        return Notification.query.get(notification_id)

    @staticmethod
    def get_by_user(user_id: int) -> List[Notification]:
        return (
            Notification.query
            .filter_by(user_id=user_id)
            .order_by(Notification.created_at.desc())
            .all()
        )

    @staticmethod
    def get_unread(user_id: int) -> List[Notification]:
        return (
            Notification.query
            .filter_by(user_id=user_id, is_read=False)
            .all()
        )

    @staticmethod
    def update() -> bool:
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def delete(notification: Notification) -> bool:
        try:
            db.session.delete(notification)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def count() -> int:
        return Notification.query.count()