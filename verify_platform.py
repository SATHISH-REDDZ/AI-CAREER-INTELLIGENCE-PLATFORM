"""
=========================================================
AI Career Intelligence Platform
Comprehensive Platform Verification Suite
=========================================================
"""

import sys
import json
from app import create_app
from app.extensions import db
from models.user import User
from models.resume import Resume
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.resume_service import ResumeService
from services.interview_service import InterviewService
from services.cover_letter_service import CoverLetterService
from services.roadmap_service import RoadmapService
from services.chatbot_service import ChatbotService
from ml.predict import MLPredictor
from nlp.parser import ResumeParser
from nlp.skill_extractor import SkillExtractor
from rag.pipeline import RAGPipeline
from chatbot.chatbot import CareerChatbotEngine


def run_verification():
    print("=========================================================")
    print("      AI CAREER INTELLIGENCE PLATFORM VERIFICATION       ")
    print("=========================================================")

    app = create_app()

    with app.app_context():
        # Create database tables
        db.create_all()
        print("[OK] Database initialized successfully.")

        # 1. Test Authentication
        print("\n--- 1. Testing User Authentication ---")
        user = UserRepository.get_by_email("testcandidate@example.com")
        if not user:
            success, msg = AuthService.register(
                full_name="Test Candidate",
                email="testcandidate@example.com",
                password="Password123!"
            )
            user = UserRepository.get_by_email("testcandidate@example.com")
            print("    Successfully created new test user.")
        else:
            print("    Retrieved existing test user.")

        assert user is not None, "User registration/retrieval failed"
        print(f"[OK] User Auth Verified (User ID: {user.id})")

        # 2. Test NLP Parser & Skill Extraction
        print("\n--- 2. Testing NLP Engine & Skill Extraction ---")
        sample_resume_text = """
        John Doe
        Email: john.doe@example.com | Phone: (555) 019-2834 | LinkedIn: linkedin.com/in/johndoe
        
        SUMMARY
        Senior Backend Engineer with 5 years experience building web applications in Python, Flask, SQL, Docker, and REST API.
        
        EXPERIENCE
        Software Engineer - Tech Solutions (2021 - Present)
        - Architected scalable microservices using Python and Flask.
        - Designed relational database schemas in PostgreSQL and SQLAlchemy.
        - Streamlined container deployment workflows with Docker and CI/CD pipelines.
        
        EDUCATION
        B.S. in Computer Science - Tech University (2020)
        
        SKILLS
        Python, Flask, PostgreSQL, Docker, REST API, Git, pytest, Redis
        """

        contact_info = ResumeParser.parse_contact_info(sample_resume_text)
        sections = ResumeParser.parse_sections(sample_resume_text)
        extracted_skills = SkillExtractor.extract_skills(sample_resume_text)

        print(f"    Parsed Contact Info: {contact_info}")
        print(f"    Extracted Skills ({len(extracted_skills)}): {extracted_skills}")
        assert "Python" in extracted_skills and "Flask" in extracted_skills
        print("[OK] NLP Engine Verified")

        # 3. Test ML Analysis & ATS Scoring Engine
        print("\n--- 3. Testing ML Analysis & ATS Scoring Engine ---")
        ml_res = MLPredictor.full_analysis(sample_resume_text, target_role="Python Developer")
        print(f"    ATS Score: {ml_res['ats_result']['ats_score']}/100")
        print(f"    Matched Skills: {ml_res['ats_result']['matched_skills']}")
        print(f"    Missing Skills: {ml_res['ats_result']['missing_skills']}")
        print(f"    Predicted Best Role: {ml_res['predicted_best_role']}")
        print(f"    Salary Estimate: {ml_res['salary_estimate']}")
        assert ml_res['ats_result']['ats_score'] > 50
        print("[OK] ML Engine Verified")

        # 4. Test Interview Preparation Service
        print("\n--- 4. Testing AI Interview Preparation Service ---")
        interview_res = InterviewService.generate_questions(user_id=user.id, target_role="Python Developer")
        print(f"    Generated Technical Questions: {len(interview_res['questions'].get('technical', []))}")
        eval_res = InterviewService.evaluate_answer(
            user_id=user.id,
            question="How do Python memory management and garbage collection work?",
            answer="Python uses reference counting and generational garbage collection to manage memory allocation and handle cyclic references."
        )
        print(f"    Answer Score: {eval_res.get('score', 0)}/100")
        assert eval_res.get('success', False) is True
        print("[OK] AI Interview Service Verified")

        # 5. Test Cover Letter & Roadmap Generators
        print("\n--- 5. Testing Cover Letter & Career Roadmap Services ---")
        cover_res = CoverLetterService.generate_cover_letter(
            user_id=user.id,
            company_name="Google DeepMind",
            job_title="AI Engineer"
        )
        print(f"    Cover Letter Generated (Len: {len(cover_res['cover_letter'])})")
        roadmap_res = RoadmapService.generate_roadmap(user_id=user.id, target_role="AI Engineer")
        print(f"    Roadmap Phases: {list(roadmap_res['roadmap'].keys())}")
        assert cover_res['success'] is True and roadmap_res['success'] is True
        print("[OK] Cover Letter & Roadmap Services Verified")

        # 6. Test RAG Pipeline & AI Career Chatbot Engine
        print("\n--- 6. Testing RAG Pipeline & Chatbot Engine ---")
        chat_res = CareerChatbotEngine.ask(
            user_id=user.id,
            query="How can I optimize my resume for ATS parsers when applying for Python Developer roles?",
            resume_text=sample_resume_text
        )
        print(f"    Chatbot Response Snapshot: {chat_res['response'][:160]}...")
        assert chat_res['success'] is True and len(chat_res['response']) > 20
        print("[OK] RAG & Chatbot Subsystem Verified")

        print("\n=========================================================")
        print("    ALL PLATFORM SUBSYSTEM VERIFICATIONS PASSED 100%!   ")
        print("=========================================================")


if __name__ == "__main__":
    run_verification()
