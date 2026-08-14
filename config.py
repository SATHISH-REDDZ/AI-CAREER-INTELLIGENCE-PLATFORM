"""
=========================================================
AI Career Intelligence Platform
Application Configuration
=========================================================
"""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False

# ---------------------------------------------------------
# Base Directory
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------

dotenv_path = BASE_DIR / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path)


def get_env(name, default=None, cast=None):
    """
    Read an environment variable and optionally cast it.
    """
    value = os.getenv(name, default)

    if value is None:
        return value

    if cast is bool:
        return str(value).strip().lower() in (
            "1",
            "true",
            "yes",
            "on",
        )

    if cast is int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    return value


class Config:
    """
    Base configuration for the application.
    """

    BASE_DIR = BASE_DIR

    # -----------------------------------------------------
    # Flask
    # -----------------------------------------------------

    SECRET_KEY = get_env(
        "SECRET_KEY",
        "change_this_secret_key"
    )

    CORS_ORIGINS = get_env("CORS_ORIGINS", "*")

    DEBUG = get_env("DEBUG", False, cast=bool)
    TESTING = get_env("TESTING", False, cast=bool)

    # -----------------------------------------------------
    # Database
    # -----------------------------------------------------

    DATABASE_PATH = BASE_DIR / "instance" / "career.db"
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    _db_url = get_env("DATABASE_URL")
    if _db_url:
        if _db_url.startswith("postgres://"):
            _db_url = _db_url.replace("postgres://", "postgresql://", 1)
        if _db_url.startswith("sqlite:///") and not _db_url.startswith("sqlite:////") and ":memory:" not in _db_url:
            rel_path = _db_url.replace("sqlite:///", "")
            if rel_path.startswith("instance/"):
                rel_path = rel_path.replace("instance/", "", 1)
            _db_url = f"sqlite:///{(BASE_DIR / 'instance' / rel_path).as_posix()}"
        SQLALCHEMY_DATABASE_URI = _db_url
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH.as_posix()}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -----------------------------------------------------
    # Gemini AI
    # -----------------------------------------------------

    GEMINI_API_KEY = get_env("GEMINI_API_KEY")

    # -----------------------------------------------------
    # JWT
    # -----------------------------------------------------

    JWT_SECRET_KEY = get_env(
        "JWT_SECRET_KEY",
        "default_fallback_jwt_secret_key_change_in_production"
    )

    # -----------------------------------------------------
    # Email
    # -----------------------------------------------------

    MAIL_SERVER = get_env("MAIL_SERVER")

    MAIL_PORT = get_env(
        "MAIL_PORT",
        587,
        cast=int
    )

    MAIL_USE_TLS = get_env(
        "MAIL_USE_TLS",
        True,
        cast=bool
    )

    MAIL_USERNAME = get_env("MAIL_USERNAME")

    MAIL_PASSWORD = get_env("MAIL_PASSWORD")

    # -----------------------------------------------------
    # Uploads
    # -----------------------------------------------------

    UPLOAD_FOLDER = str(
        BASE_DIR / get_env(
            "UPLOAD_FOLDER",
            "uploads/resumes"
        )
    )

    MAX_CONTENT_LENGTH = get_env(
        "MAX_CONTENT_LENGTH",
        16777216,
        cast=int
    )

    ALLOWED_EXTENSIONS = {
        "pdf",
        "docx"
    }

    # -----------------------------------------------------
    # Logging
    # -----------------------------------------------------

    LOG_LEVEL = get_env(
        "LOG_LEVEL",
        "INFO"
    )

    # -----------------------------------------------------
    # Application
    # -----------------------------------------------------

    APP_NAME = get_env(
        "APP_NAME",
        "AI Career Intelligence Platform"
    )

    APP_VERSION = get_env(
        "APP_VERSION",
        "1.0.0"
    )