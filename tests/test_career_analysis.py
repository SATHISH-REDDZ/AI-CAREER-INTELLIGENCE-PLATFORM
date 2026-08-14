"""
=========================================================
AI Career Intelligence Platform
AI Analysis, Skill Gap, Career Recommendation & Job Matching Tests (Phases 12-15)
=========================================================
"""

import pytest
from app.factory import create_app
from app.extensions import db
from ml.predict import MLPredictor
from ml.skill_gap import SkillGapAnalyzer, JobMatcher
from ml.career_prediction import CareerPredictor


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "test_secret_key_analysis"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


# ---------------------------------------------------------
# Phase 12: AI Resume Analysis
# ---------------------------------------------------------

def test_ai_resume_analysis_full(app):
    """Test full AI resume analysis pipeline producing structured insights."""
    sample_text = """
    Alex Taylor
    Email: alex.taylor@example.com | Phone: (555) 345-6789
    
    EXPERIENCE
    Backend Developer - TechSolutions (2021 - Present)
    - Architected REST APIs using Python, Flask, SQL, and Git.
    - Containerized microservices using Docker and deployed pytest testing suites.
    
    EDUCATION
    B.S. in Computer Science - State University
    
    SKILLS
    Python, Flask, SQL, Docker, Git, REST API, pytest
    """

    with app.app_context():
        res = MLPredictor.full_analysis(sample_text, target_role="Python Developer")

        assert "ats_result" in res
        assert "predicted_best_role" in res
        assert "skill_gap" in res
        assert "salary_estimate" in res
        assert "top_job_matches" in res

        assert res["ats_result"]["score"] >= 60.0
        assert res["predicted_best_role"] in ["Python Developer", "Backend Developer"]


# ---------------------------------------------------------
# Phase 13: Skill Gap Analysis
# ---------------------------------------------------------

def test_skill_gap_analysis_roadmap():
    """Test skill gap analysis and step-by-step progressive learning roadmap."""
    candidate_text = "I know Python, Flask, SQL, and Git."
    gap_res = SkillGapAnalyzer.analyze(candidate_text, target_role="Python Developer")

    assert gap_res["target_role"] == "Python Developer"
    assert "missing_skills" in gap_res
    assert "learning_roadmap" in gap_res

    roadmap = gap_res["learning_roadmap"]
    assert len(roadmap) > 0
    assert "step" in roadmap[0]
    assert "level" in roadmap[0]
    assert "skill" in roadmap[0]


# ---------------------------------------------------------
# Phase 14: Career Recommendation Engine
# ---------------------------------------------------------

def test_career_recommendation_roles():
    """Test multi-role career recommendation matrix."""
    skills = ["Python", "Flask", "SQL", "Docker", "REST API", "Git"]
    recommendations = CareerPredictor.recommend_roles(skills)

    assert len(recommendations) >= 3
    top_role = recommendations[0]

    assert "role" in top_role
    assert "match_percentage" in top_role
    assert "why" in top_role
    assert "missing_skills" in top_role
    assert "recommended_learning" in top_role
    assert top_role["match_percentage"] > 50.0


# ---------------------------------------------------------
# Phase 15: Custom Job Matching Engine
# ---------------------------------------------------------

def test_custom_job_description_matching():
    """Test comparing resume text against a custom Job Description text."""
    candidate_text = """
    Senior Python Developer with 4 years experience building web applications using Python, Flask, PostgreSQL, SQL, Docker, Git, and REST APIs.
    """

    job_description = """
    We are seeking a Backend Python Developer proficient in Python, Flask, PostgreSQL, Docker, AWS, and Redis. 
    Responsibilities include designing REST APIs and cloud infrastructure.
    """

    match_res = JobMatcher.match_job_description(candidate_text, job_description)

    assert "match_score" in match_res
    assert "matched_skills" in match_res
    assert "missing_skills" in match_res
    assert "recommendation" in match_res

    assert "Python" in match_res["matched_skills"]
    assert "Flask" in match_res["matched_skills"]
    assert "PostgreSQL" in match_res["matched_skills"]
    assert "AWS" in match_res["missing_skills"]
    assert match_res["match_score"] > 50.0
