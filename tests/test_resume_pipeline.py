"""
=========================================================
AI Career Intelligence Platform
Resume Upload, Parsing, NLP & ATS Pipeline Tests (Phases 8-11)
=========================================================
"""

import io
import pytest
from app.factory import create_app
from app.extensions import db
from models.user import User
from nlp.parser import ResumeParser
from nlp.skill_extractor import SkillExtractor
from ml.ats_score import ATSScoreCalculator


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "test_secret_key_pipeline",
        "JWT_SECRET_KEY": "test_jwt_secret_key_pipeline"
    })

    with app.app_context():
        db.create_all()
        # Seed test candidate
        candidate = User(
            full_name="Pipeline Candidate",
            email="pipeline@example.com"
        )
        candidate.set_password("Password123!")
        db.session.add(candidate)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_token(client):
    res = client.post("/api/auth/login", json={
        "email": "pipeline@example.com",
        "password": "Password123!"
    })
    return res.get_json()["token"]


# ---------------------------------------------------------
# Phase 8: Resume Upload Validation
# ---------------------------------------------------------

def test_resume_upload_disallowed_extension(client, auth_token):
    """Test uploading executable file returns 400."""
    headers = {"Authorization": f"Bearer {auth_token}"}
    file_data = (io.BytesIO(b"malicious executable payload"), "virus.exe")

    response = client.post(
        "/api/resumes/upload",
        data={"file": file_data},
        content_type="multipart/form-data",
        headers=headers
    )
    assert response.status_code == 400
    assert response.get_json()["success"] is False
    assert "Only PDF and DOCX" in response.get_json()["message"]


def test_resume_upload_valid_pdf_or_docx(client, auth_token):
    """Test uploading valid docx file returns 201."""
    headers = {"Authorization": f"Bearer {auth_token}"}
    content = b"John Candidate\nEmail: john@example.com\nSkills: Python, Flask, SQL, Docker, Git\nExperience: Senior Software Engineer architected microservices."
    file_data = (io.BytesIO(content), "resume.docx")

    response = client.post(
        "/api/resumes/upload",
        data={"file": file_data},
        content_type="multipart/form-data",
        headers=headers
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["success"] is True
    assert json_data["resume"]["file_type"] == "docx"


# ---------------------------------------------------------
# Phase 9: Resume Parsing
# ---------------------------------------------------------

def test_resume_parsing_contact_and_sections():
    """Test contact extraction and section segmentation."""
    sample_text = """
    Jane Doe
    Email: jane.doe@techcorp.com | Phone: (555) 234-5678 | LinkedIn: linkedin.com/in/janedoe
    
    SUMMARY
    Experienced Python Engineer.
    
    EXPERIENCE
    Senior Software Developer (2021 - Present)
    - Architected high-throughput REST APIs using Python and Flask.
    
    EDUCATION
    B.S. Computer Science - State University
    
    SKILLS
    Python, Flask, PostgreSQL, Docker, Git, REST API
    """

    contact = ResumeParser.parse_contact_info(sample_text)
    sections = ResumeParser.parse_sections(sample_text)

    assert contact["email"] == "jane.doe@techcorp.com"
    assert "linkedin.com/in/janedoe" in contact["linkedin"]
    assert "experience" in sections
    assert "education" in sections


# ---------------------------------------------------------
# Phase 10: NLP Skill Extraction
# ---------------------------------------------------------

def test_nlp_skill_extraction():
    """Test extraction of technical skills from text."""
    sample_text = "I build backend systems using Python, Flask, PostgreSQL, Docker, Git, and pytest."
    extracted = SkillExtractor.extract_skills(sample_text)

    assert "Python" in extracted
    assert "Flask" in extracted
    assert "PostgreSQL" in extracted
    assert "Docker" in extracted
    assert "Git" in extracted
    assert "pytest" in extracted


# ---------------------------------------------------------
# Phase 11: ATS Compatibility Engine
# ---------------------------------------------------------

def test_ats_score_calculation_breakdown():
    """Test ATS 7-component score calculation and JSON structure."""
    resume_text = """
    Alex Engineer
    Email: alex@example.com | Phone: (555) 987-6543
    
    EXPERIENCE
    Software Engineer - Cloud Systems (2020 - Present)
    - Architected scalable microservices using Python, Flask, and SQL.
    - Designed container deployment pipelines with Docker and Git.
    - Implemented unit test suites using pytest.
    
    EDUCATION
    Bachelor of Science in Computer Science - State University (2020)
    
    SKILLS
    Python, Flask, SQL, Git, REST API, Docker, pytest
    """

    res = ATSScoreCalculator.calculate_score(resume_text, target_role="Python Developer")

    assert "score" in res
    assert "skills_match" in res
    assert "keyword_match" in res
    assert "structure_score" in res
    assert "experience_score" in res
    assert "action_verb_score" in res
    assert "education_score" in res
    assert "formatting_score" in res
    assert "explanation" in res

    assert res["score"] >= 70.0
    assert "Python" in res["matched_skills"]
    assert len(res["explanation"]) > 20
