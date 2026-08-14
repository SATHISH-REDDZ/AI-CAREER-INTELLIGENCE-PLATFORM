# Testing & Verification Guide

The **AI Career Intelligence Platform** maintains unit, integration, and AI resilience tests using `pytest`.

---

## Running Test Suite

```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# Run all 30 tests
pytest
```

---

## Test Files & Coverage

| Test File | Focus Area |
| :--- | :--- |
| [`tests/test_auth.py`](file:///c:/Users/sathi/OneDrive/Desktop/PROJECT'S/AI-CAREER-INTELLIGENCE-PLATFORM/tests/test_auth.py) | User Registration, Password Validation, JWT Authentication, Login/Logout, Profile |
| [`tests/test_database.py`](file:///c:/Users/sathi/OneDrive/Desktop/PROJECT'S/AI-CAREER-INTELLIGENCE-PLATFORM/tests/test_database.py) | Table Creation & Entity Relationships for all 9 domain models |
| [`tests/test_resume_pipeline.py`](file:///c:/Users/sathi/OneDrive/Desktop/PROJECT'S/AI-CAREER-INTELLIGENCE-PLATFORM/tests/test_resume_pipeline.py) | Resume Upload validation, Text Parsing, NLP Skill Extraction, 7-Component ATS Score |
| [`tests/test_career_analysis.py`](file:///c:/Users/sathi/OneDrive/Desktop/PROJECT'S/AI-CAREER-INTELLIGENCE-PLATFORM/tests/test_career_analysis.py) | AI Resume Analysis, Skill Gap Roadmaps, Role Recommendations, Job Matching |
| [`tests/test_ai_features.py`](file:///c:/Users/sathi/OneDrive/Desktop/PROJECT'S/AI-CAREER-INTELLIGENCE-PLATFORM/tests/test_ai_features.py) | Chatbot Engine, RAG Retrieval, Interview Prep, Career Roadmap, Cover Letters |
| [`tests/test_integration_and_ai.py`](file:///c:/Users/sathi/OneDrive/Desktop/PROJECT'S/AI-CAREER-INTELLIGENCE-PLATFORM/tests/test_integration_and_ai.py) | Full Candidate Lifecycle Integration & Edge Case Resilience |
