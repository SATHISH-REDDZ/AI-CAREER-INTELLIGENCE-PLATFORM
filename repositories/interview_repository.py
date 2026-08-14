"""
=========================================================
AI Career Intelligence Platform
Interview Repository
=========================================================
"""

from typing import List, Optional

from app.extensions import db
from models.interview import Interview


class InterviewRepository:
    """
    Repository for Interview model.
    """

    @staticmethod
    def create(interview: Interview) -> Interview:
        db.session.add(interview)
        db.session.commit()
        return interview

    @staticmethod
    def get_by_id(interview_id: int) -> Optional[Interview]:
        return Interview.query.get(interview_id)

    @staticmethod
    def get_by_user(user_id: int) -> List[Interview]:
        return (
            Interview.query
            .filter_by(user_id=user_id)
            .order_by(Interview.created_at.desc())
            .all()
        )

    @staticmethod
    def get_all() -> List[Interview]:
        return Interview.query.order_by(Interview.created_at.desc()).all()

    @staticmethod
    def update() -> bool:
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def delete(interview: Interview) -> bool:
        try:
            db.session.delete(interview)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def count() -> int:
        return Interview.query.count()