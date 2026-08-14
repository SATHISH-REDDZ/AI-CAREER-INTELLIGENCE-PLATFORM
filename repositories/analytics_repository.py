"""
=========================================================
AI Career Intelligence Platform
Analytics Repository
=========================================================
"""

from typing import List, Optional

from app.extensions import db
from models.analytics import Analytics


class AnalyticsRepository:
    """
    Repository for Analytics model.
    """

    @staticmethod
    def create(analytics: Analytics) -> Analytics:
        db.session.add(analytics)
        db.session.commit()
        return analytics

    @staticmethod
    def get_by_id(record_id: int) -> Optional[Analytics]:
        return Analytics.query.get(record_id)

    @staticmethod
    def get_by_user(user_id: int) -> Optional[Analytics]:
        return Analytics.query.filter_by(user_id=user_id).first()

    @staticmethod
    def get_all() -> List[Analytics]:
        return Analytics.query.order_by(Analytics.created_at.desc()).all()

    @staticmethod
    def update() -> bool:
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def delete(analytics: Analytics) -> bool:
        try:
            db.session.delete(analytics)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def count() -> int:
        return Analytics.query.count()