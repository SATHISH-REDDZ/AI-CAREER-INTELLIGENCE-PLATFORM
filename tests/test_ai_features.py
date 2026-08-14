"""
=========================================================
AI Career Intelligence Platform
Chatbot, RAG, Interview, Roadmap & Cover Letter Tests (Phases 16-20)
=========================================================
"""

import pytest
from app.factory import create_app
from app.extensions import db
from models.user import User
from chatbot.chatbot import CareerChatbotEngine
from rag.pipeline import RAGPipeline
from services.interview_service import InterviewService
from services.roadmap_service import RoadmapService
from services.cover_letter_service import CoverLetterService


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "test_secret_key_ai_features",
        "JWT_SECRET_KEY": "test_jwt_secret_key_ai_features"
    })

    with app.app_context():
        db.create_all()
        # Seed test user
        user = User(
            full_name="AI Features Tester",
            email="aitester@example.com"
        )
        user.set_password("Password123!")
        db.session.add(user)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


# ---------------------------------------------------------
# Phase 16: AI Career Chatbot Engine
# ---------------------------------------------------------

def test_chatbot_context_aware_response(app):
    """Test AI career chatbot generates resume-contextual responses."""
    with app.app_context():
        user = User.query.filter_by(email="aitester@example.com").first()
        resume_text = "Experienced developer with Python, Flask, SQL, Docker, and REST API."

        res = CareerChatbotEngine.ask(
            user_id=user.id,
            query="What skills should I learn next for a Python Developer role?",
            resume_text=resume_text,
            target_role="Python Developer"
        )

        assert res["success"] is True
        assert len(res["response"]) > 20
        assert "history" in res
        assert res["conversation_id"] is not None


# ---------------------------------------------------------
# Phase 17: RAG Subsystem Pipeline
# ---------------------------------------------------------

def test_rag_retrieval_pipeline():
    """Test RAG document chunking, indexing, and context retrieval."""
    rag = RAGPipeline()
    context = rag.retrieve_context("How to prepare for technical coding interview STAR method?", top_k=2)

    assert "Technical Interview Preparation Strategy" in context or "STAR method" in context
    assert len(context) > 10


# ---------------------------------------------------------
# Phase 18: Interview Preparation Service
# ---------------------------------------------------------

def test_interview_question_generation_and_evaluation(app):
    """Test generating role interview questions and evaluating candidate answers."""
    with app.app_context():
        user = User.query.filter_by(email="aitester@example.com").first()

        # Question generation
        gen_res = InterviewService.generate_questions(user_id=user.id, target_role="Python Developer", difficulty="Medium")
        assert gen_res["success"] is True
        questions = gen_res["questions"]
        assert len(questions["technical"]) > 0
        assert len(questions["behavioral"]) > 0

        # Answer evaluation
        eval_res = InterviewService.evaluate_answer(
            user_id=user.id,
            question="Explain Flask application factory pattern.",
            answer="The application factory pattern initializes Flask applications inside a function, allowing multiple instances with different configurations for testing and production."
        )
        assert eval_res["success"] is True
        assert eval_res["score"] >= 75
        assert len(eval_res["feedback"]) > 10


# ---------------------------------------------------------
# Phase 19: Career Roadmap Generator
# ---------------------------------------------------------

def test_career_roadmap_generation(app):
    """Test generating personalized learning roadmap."""
    with app.app_context():
        user = User.query.filter_by(email="aitester@example.com").first()
        res = RoadmapService.generate_roadmap(user_id=user.id, target_role="Python Developer")

        assert res["success"] is True
        assert res["target_role"] == "Python Developer"
        assert "roadmap" in res


# ---------------------------------------------------------
# Phase 20: Cover Letter Generation with Tones
# ---------------------------------------------------------

def test_cover_letter_generation_with_tones(app):
    """Test generating tailored cover letters across different tone styles."""
    with app.app_context():
        user = User.query.filter_by(email="aitester@example.com").first()

        for tone in ["Professional", "Concise", "Technical"]:
            res = CoverLetterService.generate_cover_letter(
                user_id=user.id,
                company_name="Google DeepMind",
                job_title="Senior AI Engineer",
                job_description="Building next-gen AI applications",
                tone=tone
            )

            assert res["success"] is True
            assert res["tone"] == tone
            assert "Google DeepMind" in res["cover_letter"]
            assert len(res["cover_letter"]) > 50
