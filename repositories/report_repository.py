"""
=========================================================
AI Career Intelligence Platform
Report Repository
=========================================================
"""

from typing import List, Optional

from app.extensions import db
from models.report import Report


class ReportRepository:
    """
    Repository for Report model.
    """

    @staticmethod
    def create(report: Report) -> Report:
        db.session.add(report)
        db.session.commit()
        return report

    @staticmethod
    def get_by_id(report_id: int) -> Optional[Report]:
        return Report.query.get(report_id)

    @staticmethod
    def get_by_user(user_id: int) -> List[Report]:
        return (
            Report.query
            .filter_by(user_id=user_id)
            .order_by(Report.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_resume(resume_id: int) -> List[Report]:
        return Report.query.filter_by(resume_id=resume_id).all()

    @staticmethod
    def get_all() -> List[Report]:
        return Report.query.order_by(Report.created_at.desc()).all()

    @staticmethod
    def update() -> bool:
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def delete(report: Report) -> bool:
        try:
            db.session.delete(report)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def count() -> int:
        return Report.query.count()