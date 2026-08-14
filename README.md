# AI Career Intelligence Platform 🚀

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Flask Framework](https://img.shields.io/badge/framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![GenAI SDK](https://img.shields.io/badge/AI-Google_GenAI_SDK-orange.svg)](https://pypi.org/project/google-genai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A production-oriented AI-powered career intelligence platform built with Python 3.12, Flask, NLP, machine learning, FAISS vector RAG, and generative AI.

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Solution](#3-solution)
4. [Key Features](#4-key-features)
5. [System Architecture](#5-system-architecture)
6. [Tech Stack](#6-tech-stack)
7. [Project Structure](#7-project-structure)
8. [AI & ML Pipeline](#8-ai--ml-pipeline)
9. [Database Architecture](#9-database-architecture)
10. [API Documentation](#10-api-documentation)
11. [Installation](#11-installation)
12. [Environment Variables](#12-environment-variables)
13. [Running Locally](#13-running-locally)
14. [Testing](#14-testing)
15. [Docker Containerization](#15-docker-containerization)
16. [Dashboard & UI Walkthrough](#16-dashboard--ui-walkthrough)
17. [Live Demonstration](#17-live-demonstration)
18. [Deployment Guide](#18-deployment-guide)
19. [Future Improvements](#19-future-improvements)
20. [License](#20-license)

---

## 1. Project Overview
The **AI Career Intelligence Platform** empowers job seekers and professionals with data-driven career optimization tools. By combining NLP text processing, 7-component weighted ATS scoring, FAISS vector store search, and Google GenAI LLMs, the platform turns unstructured resume files into actionable career advancement roadmaps.

---

## 2. Problem Statement
Job seekers face significant hurdles in today's recruitment landscape:
- **Opaque ATS Systems**: 75%+ of resumes are discarded by Applicant Tracking Systems before human review.
- **Unclear Skill Gaps**: Candidates lack precise visibility into missing skills required for target roles.
- **Generic Feedback**: Standard career advice fails to address candidate-specific experience and goals.

---

## 3. Solution
Our platform provides an end-to-end intelligence suite:
- **Resume Upload & Parsing**: Validates `.pdf` and `.docx` uploads and extracts structured contact info and sections.
- **7-Component ATS Scoring**: Scores candidate compatibility across Skills (35%), Keywords (20%), Structure (15%), Experience (10%), Verbs (10%), Education (5%), and Formatting (5%).
- **AI Skill-Gap Roadmaps**: Generates progressive step-by-step learning roadmaps (*Beginner* → *Intermediate* → *Advanced* → *Cloud*).
- **Custom Job Matching**: Compares candidate resumes against raw Job Descriptions (calculating skill overlap ✓ / ✗ and text similarity).
- **FAISS RAG Career Chatbot**: Interactively answers career queries grounded in FAISS vector store search and candidate profile context.
- **AI Mock Interview Preparation**: Generates role-specific question sets and evaluates candidate answers out of 100 with actionable feedback.
- **Cover Letter Generator**: Generates customized cover letters in *Professional*, *Concise*, or *Technical* tone styles.

---

## 4. Key Features

| Feature | Description |
| :--- | :--- |
| **Authentication & JWT** | Secure user registration, password hashing (`pbkdf2:sha256`), and JWT token protection |
| **Resume Upload Engine** | Multi-format PDF/DOCX parsing, MIME type checking, size validation, and `secure_filename` storage |
| **NLP Skill Extraction** | Regex & tokenization engine extracting 40+ technical skills from resume text |
| **7-Component ATS Score** | Weighted algorithm scoring Skills (35%), Keywords (20%), Structure (15%), Experience (10%), Verbs (10%), Education (5%), Formatting (5%) |
| **AI Resume Analysis** | Google GenAI SDK integration producing summaries, strengths, weaknesses, recommended roles, and salary ranges |
| **Custom Job Matching** | Compares candidate resume text directly against target Job Descriptions with skill overlap breakdown |
| **FAISS RAG Career Coach** | Contextual chatbot backed by FAISS vector embeddings and dense L2 similarity search |
| **Mock Interview Suite** | Question generation and AI answer scoring with qualitative feedback |
| **Cover Letter Generator** | Tone-customizable cover letter writer (*Professional*, *Concise*, *Technical*) |
| **Interactive Dashboard** | Analytics overview showing ATS score history, skill match %, and quick action links |

---

## 5. System Architecture

```
                         ┌──────────────────┐
                         │     Frontend     │
                         │ Dashboard/UI     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Flask API     │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
        Authentication       Resume Engine       Career Engine
              │                   │                   │
              │             ┌─────┴─────┐       ┌─────┴─────┐
              │             ▼           ▼       ▼           ▼
              │            NLP         ATS    Jobs      Interview
              │             │           │       │           │
              └─────────────┴───────────┴───────┴───────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Google GenAI   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    FAISS RAG     │
                         │ Vector Retrieval │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    PostgreSQL    │
                         │     / SQLite     │
                         └──────────────────┘
```

---

## 6. Tech Stack

- **Backend Framework**: Python 3.12 / Flask 3.0
- **Database**: SQLAlchemy 2.0 / Flask-Migrate / SQLite (Dev) / PostgreSQL (Prod)
- **Security & Auth**: Werkzeug Password Hashing / PyJWT / Flask-Cors / Werkzeug ProxyFix
- **NLP & Parsing**: PyPDF2 / pdfplumber / python-docx / NLTK / Regex
- **Machine Learning**: Scikit-Learn / NumPy / Pandas
- **Generative AI & RAG**: Google GenAI SDK (`from google import genai`) / FAISS (`faiss-cpu`) / LangChain
- **Production Web Server**: Gunicorn
- **Containerization & CI/CD**: Docker / Docker Compose / GitHub Actions

---

## 7. Project Structure

```
AI-Career-Intelligence-Platform/
│
├── app/                  # Flask application factory, extensions, middleware, error handlers
├── ai/                   # AI integration wrappers & roadmap generators
├── chatbot/              # Chatbot engine, conversational memory & context builders
├── controllers/          # Request controllers (Auth, Resume, Analytics, etc.)
├── core/                 # Core logging & system setup
├── database/             # Database initialization & base models
├── docs/                 # System architecture, API, database, security docs
├── ml/                   # ML ATS scoring calculator, skill gap & career predictor
├── models/               # SQLAlchemy domain models (User, Resume, Job, Report, etc.)
├── nlp/                  # Section parser, skill extractor, keyword matcher, similarity engine
├── rag/                  # FAISS RAG document loader, vector embeddings & retrieval index
├── repositories/         # Database repositories (User, Resume, Chatbot, etc.)
├── routes/               # API Blueprint routes (Auth, Resume, Interview, Chatbot, etc.)
├── schemas/              # Input validation schemas
├── services/             # Core business logic services
├── static/               # CSS, JavaScript & static assets
├── templates/            # HTML dashboard & landing templates
├── tests/                # Pytest unit & integration test suite
├── uploads/              # File upload storage
├── utils/                # Password, JWT & file validation helpers
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── Dockerfile            # Production Docker image build file (python:3.12-slim)
├── docker-compose.yml    # Docker Compose multi-service setup
├── Procfile              # Gunicorn deployment configuration
├── pytest.ini            # Pytest test configuration
├── README.md             # Platform documentation
├── requirements.txt      # Production python dependencies
├── run.py                # Local development entrypoint
├── verify_platform.py    # Subsystem verification script
└── wsgi.py               # WSGI production entrypoint
```

---

## 8. AI & ML Pipeline
See detailed AI documentation in [`docs/ai-pipeline.md`](docs/ai-pipeline.md).

---

## 9. Database Architecture
See database schema documentation in [`docs/database.md`](docs/database.md).

---

## 10. API Documentation
See full REST API endpoints documentation in [`docs/api.md`](docs/api.md).

---

## 11. Installation

```bash
# 1. Clone repository
git clone https://github.com/user/ai-career-platform.git
cd ai-career-platform

# 2. Create virtual environment (Python 3.12)
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 4. Upgrade pip & install requirements
pip install -r requirements.txt
```

---

## 12. Environment Variables
Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Configure key settings in `.env`:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here
DATABASE_URL=sqlite:///instance/career.db
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
CORS_ORIGINS=*
```

---

## 13. Running Locally

```bash
python run.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 14. Testing

Run full test suite (30 automated unit & integration tests):

```bash
pytest
```

---

## 15. Docker Containerization

```bash
# Build Docker image
docker build -t ai-career-platform .

# Run Docker container
docker run -p 5000:5000 ai-career-platform
```

Or using Docker Compose:
```bash
docker-compose up -d
```

---

## 16. Dashboard & UI Walkthrough
Access the candidate dashboard at `/templates/dashboard.html` or `/api/analytics/dashboard` to view ATS score progression, skill match percentages, and quick-action links.

---

## 17. Live Demonstration
Run the automated platform verification suite:

```bash
python verify_platform.py
```

---

## 18. Deployment Guide
See deployment procedures for Render, Railway, and Cloud Run in [`docs/deployment.md`](docs/deployment.md).

---

## 19. Future Improvements
- Automated LinkedIn profile scraping integration.
- Real-time video mock interview speech-to-text analysis.
- Multi-language resume parsing support.

---

## 20. License
Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
