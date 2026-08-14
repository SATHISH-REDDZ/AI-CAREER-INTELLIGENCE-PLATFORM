"""
=========================================================
AI Career Intelligence Platform
Flask Extensions
=========================================================
"""

from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# ---------------------------------------------------------
# Database
# ---------------------------------------------------------

db = SQLAlchemy()

# ---------------------------------------------------------
# Database Migration
# ---------------------------------------------------------

migrate = Migrate()

# ---------------------------------------------------------
# Login Manager
# ---------------------------------------------------------

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Please login to continue."
login_manager.login_message_category = "warning"

# ---------------------------------------------------------
# CSRF Protection
# ---------------------------------------------------------

csrf = CSRFProtect()

# ---------------------------------------------------------
# Cross-Origin Resource Sharing (CORS)
# ---------------------------------------------------------

cors = CORS()


def initialize_extensions(app):
    """
    Initialize all Flask extensions.

    Args:
        app (Flask): Flask application instance.
    """

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        try:
            from models.user import User
            return db.session.get(User, int(user_id))
        except Exception:
            return None

    origins = app.config.get("CORS_ORIGINS", "*")
    if isinstance(origins, str) and "," in origins:
        origins = [o.strip() for o in origins.split(",")]

    cors.init_app(
        app,
        resources={r"/*": {"origins": origins}}
    )