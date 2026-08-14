"""
=========================================================
AI Career Intelligence Platform
Resume & API Integration Tests
=========================================================
"""

import io
import pytest
from app.factory import create_app
from app.extensions import db
from models.user import User


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test_secret_key"
    })

    with app.app_context():
        db.create_all()
        # Seed test user
        user = User(
            full_name="Test Candidate",
            email="candidate@example.com",
            role="user"
        )
        user.set_password("Password123!")
        db.session.add(user)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_token(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "candidate@example.com", "password": "Password123!"}
    )
    data = response.get_json()
    return data.get("token") or data.get("access_token")


def test_home_and_health(client):
    res_home = client.get("/")
    assert res_home.status_code == 200

    res_version = client.get("/version")
    assert res_version.status_code == 200
    assert "application" in res_version.get_json()

    res_health = client.get("/health")
    assert res_health.status_code == 200
    assert res_health.get_json()["status"] == "Healthy"


def test_resume_upload_and_analysis(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Upload test resume text as txt/pdf sample
    file_data = (io.BytesIO(b"Candidate Resume\nSkills: Python, Flask, SQL, Machine Learning\nExperience: Backend Developer"), "test_resume.docx")

    res_upload = client.post(
        "/api/resumes/upload",
        data={"file": file_data},
        content_type="multipart/form-data",
        headers=headers
    )
    assert res_upload.status_code == 201
    json_upload = res_upload.get_json()
    assert json_upload["success"] is True
    resume_id = json_upload["resume"]["id"]

    # Analyze resume
    res_analyze = client.post(
        f"/api/resumes/{resume_id}/analyze",
        json={"target_role": "Python Developer"},
        headers=headers
    )
    assert res_analyze.status_code == 200
    json_analyze = res_analyze.get_json()
    assert json_analyze["success"] is True
    assert "ats_score" in json_analyze["resume"]

    # Get user resumes list
    res_list = client.get("/api/resumes", headers=headers)
    assert res_list.status_code == 200
    assert len(res_list.get_json()["resumes"]) == 1
