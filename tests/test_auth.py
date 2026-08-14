"""
=========================================================
AI Career Intelligence Platform
Authentication Unit & Integration Tests (Phase 7)
=========================================================
"""

import pytest
from app.factory import create_app
from app.extensions import db
from models.user import User


@pytest.fixture
def app():
    """Configure test application with in-memory database."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "test_secret_key",
        "JWT_SECRET_KEY": "test_jwt_secret_key"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_register_valid_user(client):
    """Test valid user registration returns 201."""
    response = client.post("/api/auth/register", json={
        "full_name": "John Candidate",
        "email": "john.candidate@example.com",
        "password": "Password123!"
    })

    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "registered successfully" in json_data["message"]


def test_register_duplicate_email(client):
    """Test registering with duplicate email returns 400."""
    client.post("/api/auth/register", json={
        "full_name": "John Candidate",
        "email": "john.candidate@example.com",
        "password": "Password123!"
    })

    response = client.post("/api/auth/register", json={
        "full_name": "John Duplicate",
        "email": "john.candidate@example.com",
        "password": "Password123!"
    })

    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["success"] is False
    assert "already exists" in json_data["message"].lower()


def test_register_invalid_email(client):
    """Test registering with invalid email format returns 400."""
    response = client.post("/api/auth/register", json={
        "full_name": "Bad Email",
        "email": "invalid-email-format",
        "password": "Password123!"
    })

    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["success"] is False
    assert "invalid email" in json_data["message"].lower()


def test_register_weak_password(client):
    """Test registering with weak password returns 400."""
    response = client.post("/api/auth/register", json={
        "full_name": "Weak Pass",
        "email": "weak@example.com",
        "password": "123"
    })

    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["success"] is False
    assert "not strong enough" in json_data["message"].lower()


def test_login_correct_credentials(client):
    """Test login with correct credentials returns token and 200."""
    client.post("/api/auth/register", json={
        "full_name": "Login User",
        "email": "login@example.com",
        "password": "Password123!"
    })

    response = client.post("/api/auth/login", json={
        "email": "login@example.com",
        "password": "Password123!"
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "token" in json_data


def test_login_wrong_password(client):
    """Test login with wrong password returns 401."""
    client.post("/api/auth/register", json={
        "full_name": "Login User",
        "email": "login@example.com",
        "password": "Password123!"
    })

    response = client.post("/api/auth/login", json={
        "email": "login@example.com",
        "password": "WrongPassword!"
    })

    assert response.status_code == 401
    json_data = response.get_json()
    assert json_data["success"] is False


def test_unauthorized_profile_request(client):
    """Test profile endpoint without authorization header returns 401."""
    response = client.get("/api/auth/profile")
    assert response.status_code == 401


def test_authorized_profile_request(client):
    """Test profile endpoint with valid JWT token returns 200."""
    client.post("/api/auth/register", json={
        "full_name": "Profile User",
        "email": "profile@example.com",
        "password": "Password123!"
    })

    login_res = client.post("/api/auth/login", json={
        "email": "profile@example.com",
        "password": "Password123!"
    })
    token = login_res.get_json()["token"]

    response = client.get(
        "/api/auth/profile",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert json_data["user"]["email"] == "profile@example.com"
