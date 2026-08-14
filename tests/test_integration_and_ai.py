"""
=========================================================
AI Career Intelligence Platform
Integration & AI Resilient Edge Case Tests (Phases 24 & 25)
=========================================================
"""

import io
import pytest
from app.factory import create_app
from app.extensions import db
from models.user import User
from ml.ats_score import ATSScoreCalculator
from services.resume_service import ResumeService
from chatbot.chatbot import CareerChatbotEngine


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "integration_ai_secret_key_testing_2026",
        "JWT_SECRET_KEY": "integration_ai_jwt_secret_key_testing_2026",
        "GEMINI_API_KEY": None  # Test resilient handling when key is not set
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# ---------------------------------------------------------
# Phase 24: End-to-End Integration Journey & HTTP Status Codes
# ---------------------------------------------------------

def test_full_user_candidate_journey(client):
    """
    Test End-to-End Candidate Journey:
    1. Register
    2. Login
    3. Upload Resume
    4. Analyze Resume
    5. Fetch Dashboard Analytics
    """
    # 1. Register candidate (201)
    reg_res = client.post("/api/auth/register", json={
        "full_name": "Integration Candidate",
        "email": "integration.user@example.com",
        "password": "Password123!"
    })
    assert reg_res.status_code == 201

    # 2. Login candidate (200)
    login_res = client.post("/api/auth/login", json={
        "email": "integration.user@example.com",
        "password": "Password123!"
    })
    assert login_res.status_code == 200
    token = login_res.get_json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Upload Resume (201)
    resume_payload = b"Integration User\nSkills: Python, Flask, SQL, Docker, Git\nExperience: Built microservices."
    file_data = (io.BytesIO(resume_payload), "candidate_resume.pdf")

    upload_res = client.post(
        "/api/resumes/upload",
        data={"file": file_data},
        content_type="multipart/form-data",
        headers=headers
    )
    assert upload_res.status_code == 201
    resume_id = upload_res.get_json()["resume"]["id"]

    # 4. Analyze Resume (200)
    analyze_res = client.post(
        f"/api/resumes/{resume_id}/analyze",
        json={"target_role": "Python Developer"},
        headers=headers
    )
    assert analyze_res.status_code == 200
    assert analyze_res.get_json()["resume"]["ats_score"] > 50

    # 5. Get Dashboard Analytics (200)
    dash_res = client.get("/api/analytics/dashboard", headers=headers)
    assert dash_res.status_code == 200
    analytics = dash_res.get_json()["analytics"]
    assert analytics["total_resumes_uploaded"] == 1
    assert "quick_actions" in analytics


def test_api_status_codes_and_error_formatting(client):
    """Test standard HTTP status code responses (400, 401, 404)."""
    # 404 Not Found
    res_404 = client.get("/api/non-existent-endpoint")
    assert res_404.status_code == 404
    assert res_404.get_json()["success"] is False

    # 401 Unauthorized
    res_401 = client.get("/api/auth/profile")
    assert res_401.status_code == 401
    assert res_401.get_json()["success"] is False

    # 400 Bad Request
    res_400 = client.post("/api/auth/register", json={})
    assert res_400.status_code == 400
    assert res_400.get_json()["success"] is False


# ---------------------------------------------------------
# Phase 25: AI Resilient Edge Case Testing
# ---------------------------------------------------------

def test_ai_resilience_empty_resume(app):
    """Test ATS and chatbot gracefully handling empty resume text without crashing."""
    res = ATSScoreCalculator.calculate_score("", target_role="Python Developer")
    assert res["score"] == 0.0
    assert len(res["missing_skills"]) > 0
    assert "Empty resume text" in res["explanation"]


def test_ai_resilience_unusual_formatting_and_large_resume(app):
    """Test system handling very large resume text and strange symbols gracefully."""
    large_resume = "Python Flask SQL Docker Git " * 1000 + " !!! @@@ ### $$$ %%% ^^^ *** "
    res = ATSScoreCalculator.calculate_score(large_resume, target_role="Python Developer")

    assert res["score"] > 0
    assert "Python" in res["matched_skills"]


def test_ai_resilience_no_gemini_api_key(app):
    """Test chatbot engine gracefully falling back when GEMINI_API_KEY is absent."""
    with app.app_context():
        user = User(
            full_name="Fallback Candidate",
            email="fallback@example.com"
        )
        user.set_password("Password123!")
        db.session.add(user)
        db.session.commit()

        chat_res = CareerChatbotEngine.ask(
            user_id=user.id,
            query="What should I study for Python Developer roles?",
            resume_text="Skills: Python, SQL"
        )

        assert chat_res["success"] is True
        assert len(chat_res["response"]) > 10
        assert chat_res["conversation_id"] is not None
