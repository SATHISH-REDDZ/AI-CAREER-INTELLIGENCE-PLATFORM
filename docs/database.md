# Database Architecture - AI Career Intelligence Platform

## Schema Overview

The database is built with SQLAlchemy ORM and supports SQLite for local development and PostgreSQL for production.

```
+---------------+        +---------------+        +---------------+
|     User      |------->|    Resume     |------->|    Report     |
+---------------+ 1    * +---------------+ 1    * +---------------+
        |                        |
        | 1                      | 1
        v *                      v *
+---------------+        +---------------+
| Conversation  |        |    Analytics  |
+---------------+        +---------------+
```

## Core Models

1. **User (`users`)**: Stores user credentials, password hash, email verification status, and role (`user`/`admin`).
2. **Resume (`resumes`)**: Contains file upload metadata, extracted text, section data, ATS score, missing skills JSON, and AI summaries.
3. **Job (`jobs`)**: Stores target job descriptions, skill requirements, and candidate matching scores.
4. **Skill (`skills`)**: Taxonomy of technical and soft skills mapped to industry roles.
5. **Interview (`interviews`)**: AI-generated interview questions, user responses, evaluation scores, and feedback.
6. **Conversation (`conversations`)**: Chatbot query logs, responses, model used, response time, and token counts.
7. **Report (`reports`)**: Persistent generated PDF/JSON career intelligence audit reports.
8. **Analytics (`analytics`)**: User activity metrics, ATS score progression, and platform usage statistics.
9. **Notification (`notifications`)**: User alerts for resume processing, recommendations, and system events.
