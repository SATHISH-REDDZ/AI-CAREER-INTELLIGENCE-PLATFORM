"""
=========================================================
AI Career Intelligence Platform
Job Repository
=========================================================
"""

from typing import List, Optional

from app.extensions import db
from models.job import Job


class JobRepository:
    """
    Repository for Job model.
    """

    @staticmethod
    def create(job: Job) -> Job:
        db.session.add(job)
        db.session.commit()
        return job

    @staticmethod
    def get_by_id(job_id: int) -> Optional[Job]:
        return Job.query.get(job_id)

    @staticmethod
    def get_all() -> List[Job]:
        return Job.query.order_by(Job.created_at.desc()).all()

    @staticmethod
    def search(title: str) -> List[Job]:
        return (
            Job.query
            .filter(Job.title.ilike(f"%{title}%"))
            .all()
        )

    @staticmethod
    def get_active_jobs() -> List[Job]:
        return Job.query.filter_by(is_active=True).all()

    @staticmethod
    def update() -> bool:
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def delete(job: Job) -> bool:
        try:
            db.session.delete(job)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def count() -> int:
        return Job.query.count()