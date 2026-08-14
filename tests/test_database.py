"""
=========================================================
AI Career Intelligence Platform
Database Model Verification Tests (Phase 6)
=========================================================
"""

import pytest
from app.factory import create_app
from app.extensions import db
from models import (
    User,
    Resume,
    Job,
    Skill,
    Report,
    Analytics,
    Interview,
    Conversation,
    Notification,
)


@pytest.fixture
def app():
    """Configure application for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_database_table_creation(app):
    """Test that all 9 domain models create their tables successfully."""
    with app.app_context():
        # Verify user model
        user = User(
            full_name="Database Test User",
            email="dbtest@example.com"
        )
        user.set_password("Password123!")
        db.session.add(user)
        db.session.commit()

        assert user.id is not None
        assert user.password_hash != "Password123!"

        # Verify resume model relationship
        resume = Resume(
            user_id=user.id,
            file_name="test_resume.pdf",
            file_path="/uploads/test_resume.pdf",
            file_type="pdf",
            file_size=1024
        )
        db.session.add(resume)
        db.session.flush()

        # Verify job model
        job = Job(
            title="Senior Python Engineer",
            company="Tech Corp",
            description="Python Flask Developer role"
        )
        db.session.add(job)

        # Verify skill model
        skill = Skill(name="Python", category="Programming Language")
        db.session.add(skill)

        # Verify report model
        report = Report(
            user_id=user.id,
            resume_id=resume.id,
            report_name="ATS Compatibility Report",
            overall_score=88.5,
            ats_score=90.0
        )
        db.session.add(report)

        # Verify analytics model
        analytics = Analytics(
            user_id=user.id,
            resumes_uploaded=1,
            reports_generated=1,
            average_resume_score=88.5,
            average_ats_score=90.0
        )
        db.session.add(analytics)

        # Verify interview model
        interview = Interview(
            user_id=user.id,
            interview_type="Technical",
            score=85.0
        )
        db.session.add(interview)

        # Verify conversation model
        conv = Conversation(
            user_id=user.id,
            question="What skills should I learn?",
            answer="Learn Docker and PostgreSQL."
        )
        db.session.add(conv)

        # Verify notification model
        notif = Notification(
            user_id=user.id,
            title="Welcome",
            message="Welcome to AI Career Platform!"
        )
        db.session.add(notif)

        db.session.commit()

        # Query and assert persistence across all 9 tables
        assert User.query.count() == 1
        assert Resume.query.count() == 1
        assert Job.query.count() == 1
        assert Skill.query.count() == 1
        assert Report.query.count() == 1
        assert Analytics.query.count() == 1
        assert Interview.query.count() == 1
        assert Conversation.query.count() == 1
        assert Notification.query.count() == 1
