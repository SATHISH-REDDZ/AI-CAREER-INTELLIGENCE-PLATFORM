# Deployment Guide

This guide outlines deployment procedures for the **AI Career Intelligence Platform** on Render, Railway, Google Cloud Run, and Docker containers.

---

## Environment Variables Configuration

Set the following environment variables in your hosting environment:

| Key | Example Value | Description |
| :--- | :--- | :--- |
| `FLASK_APP` | `run.py` | Flask entrypoint |
| `FLASK_ENV` | `production` | Set environment mode |
| `DEBUG` | `False` | Disable debug mode in production |
| `SECRET_KEY` | `strong_random_secret_key_32_bytes` | Flask session secret |
| `JWT_SECRET_KEY` | `strong_random_jwt_secret_key_32_bytes` | JWT token secret |
| `DATABASE_URL` | `postgresql://user:pass@host:5432/dbname` | Production PostgreSQL URI |
| `GEMINI_API_KEY` | `AIzaSy...` | Google Gemini API Key |
| `UPLOAD_FOLDER` | `uploads/resumes` | Storage path for uploads |
| `LOG_LEVEL` | `INFO` | Logging level |

---

## 1. Deploying on Render

1. Connect your GitHub repository to [Render](https://render.com).
2. Create a new **Web Service**.
3. Set **Environment**: `Docker` or `Python 3`.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn wsgi:app --bind 0.0.0.0:$PORT`
6. Attach a Render **PostgreSQL** database and pass `DATABASE_URL`.

---

## 2. Deploying on Railway

1. Create a new project on [Railway](https://railway.app).
2. Choose **Deploy from GitHub repo**.
3. Add a **PostgreSQL** service to the project.
4. Add environment variables to the web service (`JWT_SECRET_KEY`, `SECRET_KEY`, `GEMINI_API_KEY`).
5. Railway will automatically build via `Dockerfile` or `Procfile`.

---

## 3. Deploying via Docker

```bash
# Build Docker image
docker build -t ai-career-platform .

# Run container locally
docker run -d -p 5000:5000 \
  -e SECRET_KEY="prod_secret" \
  -e JWT_SECRET_KEY="prod_jwt_secret" \
  -e GEMINI_API_KEY="your_api_key" \
  ai-career-platform
```

Or using Docker Compose:

```bash
docker-compose up -d --build
```
