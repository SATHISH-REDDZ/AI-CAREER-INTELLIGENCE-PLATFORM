# API Documentation - AI Career Intelligence Platform

## Base URL
- Development: `http://127.0.0.1:5000/api`
- Production: `https://your-domain.com/api`

---

## Authentication Endpoints

### 1. Register User
- **POST** `/auth/register`
- **Request Body**:
  ```json
  {
    "full_name": "John Doe",
    "email": "john@example.com",
    "password": "Password123!"
  }
  ```
- **Response (201)**:
  ```json
  {
    "success": true,
    "message": "User registered successfully."
  }
  ```

### 2. User Login
- **POST** `/auth/login`
- **Request Body**:
  ```json
  {
    "email": "john@example.com",
    "password": "Password123!"
  }
  ```
- **Response (200)**:
  ```json
  {
    "success": true,
    "token": "<JWT_BEARER_TOKEN>"
  }
  ```

---

## Resume Endpoints

### 1. Upload Resume
- **POST** `/resumes/upload`
- **Headers**: `Authorization: Bearer <token>`
- **Form Data**: `file` (PDF/DOCX)
- **Response (201)**:
  ```json
  {
    "success": true,
    "resume": {
      "id": 1,
      "file_name": "resume.pdf",
      "status": "Parsed"
    }
  }
  ```

### 2. Analyze Resume & ATS Scoring
- **POST** `/resumes/{id}/analyze`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "target_role": "Python Developer"
  }
  ```
- **Response (200)**:
  ```json
  {
    "success": true,
    "resume": {
      "id": 1,
      "ats_score": 82.5,
      "skill_match": 85.0,
      "missing_skills": ["Docker", "PostgreSQL"],
      "recommended_role": "Python Developer"
    }
  }
  ```

---

## Chatbot & RAG Endpoints

### 1. Ask Chatbot
- **POST** `/chatbot/query`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "query": "What skills should I learn next for a Backend Developer role?",
    "persona": "Career Advisor"
  }
  ```
- **Response (200)**:
  ```json
  {
    "success": true,
    "response": "Based on your current resume...",
    "suggestions": ["How to prepare for Docker interviews?", "What projects build backend experience?"]
  }
  ```
