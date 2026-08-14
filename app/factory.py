"""
=========================================================
AI Career Intelligence Platform
Application Factory
=========================================================
"""
from flask import Flask

from config import Config
from app.extensions import initialize_extensions
from app.middleware import register_middleware
from app.errors import register_error_handlers
from core.logging import setup_logging
from database.database import initialize_database


def create_app() -> Flask:
    """
    Create and configure the Flask application.
    """

    app = Flask(
        __name__,
        template_folder=str(Config.BASE_DIR / "templates"),
        static_folder=str(Config.BASE_DIR / "static")
    )

    # Load configuration
    app.config.from_object(Config)

    # Initialize logging
    setup_logging()

    # Initialize Flask extensions
    initialize_extensions(app)

    # Register middleware
    register_middleware(app)

    # Register error handlers
    register_error_handlers(app)

    # Initialize database
    initialize_database(app)

    # Register application routes
    from app.routes import register_routes
    register_routes(app)

    # Register API Blueprints
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    from routes.admin_routes import admin_bp
    from routes.resume_routes import resume_bp
    from routes.interview_routes import interview_bp
    from routes.analytics_routes import analytics_bp
    from routes.cover_letter_routes import cover_letter_bp
    from routes.roadmap_routes import roadmap_bp
    from routes.chatbot_routes import chatbot_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(cover_letter_bp)
    app.register_blueprint(roadmap_bp)
    app.register_blueprint(chatbot_bp)

    # Return the configured application
    return app