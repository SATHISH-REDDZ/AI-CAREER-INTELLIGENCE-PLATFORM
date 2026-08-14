# System Architecture - AI Career Intelligence Platform

## Architecture Overview

The **AI Career Intelligence Platform** follows a modular, multi-layer enterprise architecture using Flask, SQLAlchemy, NLP/ML engines, and Google Gemini LLM integrations.

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
                         │   AI / Gemini    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │       RAG        │
                         │ Vector Retrieval │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ SQLAlchemy / DB  │
                         └──────────────────┘
```

## Layers

1. **Presentation / Web Layer (`templates/`, `static/`, `app/routes.py`)**: Renders Jinja2 HTML templates and provides interactive user dashboards.
2. **API & Route Layer (`routes/`, `controllers/`)**: Handles REST requests, JSON validation, HTTP responses, and routing.
3. **Business Logic Layer (`services/`)**: Implements auth, resume processing, chatbot, interview prep, cover letter generation, and recommendations.
4. **NLP & ML Core (`nlp/`, `ml/`, `ai/`)**: Section detection, skill extraction, ATS weighted calculation, job matching, and Gemini LLM prompt pipelines.
5. **Data Access Layer (`models/`, `repositories/`, `database/`)**: Manages SQLAlchemy ORM models, migrations, and database connections.
