"""
=========================================================
AI Career Intelligence Platform
Application Routes
=========================================================
"""

from flask import Flask, jsonify, render_template


def register_routes(app: Flask) -> None:
    """
    Register application Web & System routes.

    Args:
        app (Flask): Flask application instance.
    """

    @app.route("/", methods=["GET"])
    @app.route("/chatbot", methods=["GET"])
    @app.route("/ats", methods=["GET"])
    @app.route("/interview", methods=["GET"])
    @app.route("/jobs", methods=["GET"])
    @app.route("/cover-letter", methods=["GET"])
    @app.route("/dashboard", methods=["GET"])
    def home():
        """
        Home & Chatbot Web UI Dashboard Page.
        """
        return render_template("landing.html")

    @app.route("/google-login", methods=["GET"])
    def google_login_page():
        """
        Google Accounts OAuth Consent & Account Chooser.
        """
        return render_template("google_login.html")

    @app.route("/health", methods=["GET"])
    def health():
        """
        Health check endpoint.
        """
        return jsonify(
            {
                "status": "Healthy",
                "message": "Application is running successfully.",
            }
        )

    @app.route("/version", methods=["GET"])
    def version():
        """
        Application version endpoint.
        """
        return jsonify(
            {
                "application": app.config.get("APP_NAME"),
                "version": app.config.get("APP_VERSION"),
            }
        )