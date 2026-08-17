"""
=========================================================
AI Career Intelligence Platform
Application Web Routes Blueprint
=========================================================
"""

from flask import Blueprint, jsonify, render_template

web_bp = Blueprint("web", __name__)


@web_bp.route("/", methods=["GET"])
@web_bp.route("/chatbot", methods=["GET"])
def home():
    """
    Main SPA Chatbot & AI Assistant Dashboard.
    """
    return render_template("landing.html")


@web_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@web_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@web_bp.route("/dashboard", methods=["GET"])
def dashboard_page():
    return render_template("dashboard.html")


@web_bp.route("/profile", methods=["GET"])
def profile_page():
    return render_template("profile.html")


@web_bp.route("/upload-resume", methods=["GET"])
def upload_resume_page():
    return render_template("upload_resume.html")


@web_bp.route("/ats", methods=["GET"])
@web_bp.route("/resume-analysis", methods=["GET"])
def ats_page():
    return render_template("ats_report.html")


@web_bp.route("/interview", methods=["GET"])
def interview_page():
    return render_template("interview.html")


@web_bp.route("/jobs", methods=["GET"])
def jobs_page():
    return render_template("dashboard.html")


@web_bp.route("/roadmap", methods=["GET"])
def roadmap_page():
    return render_template("roadmap.html")


@web_bp.route("/cover-letter", methods=["GET"])
def cover_letter_page():
    return render_template("cover_letter.html")


@web_bp.route("/analytics", methods=["GET"])
def analytics_page():
    return render_template("analytics.html")


@web_bp.route("/settings", methods=["GET"])
def settings_page():
    return render_template("settings.html")


@web_bp.route("/history", methods=["GET"])
def history_page():
    return render_template("history.html")


@web_bp.route("/reports", methods=["GET"])
def reports_page():
    return render_template("reports.html")


@web_bp.route("/google-login", methods=["GET"])
def google_login_page():
    return render_template("google_login.html")


@web_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Healthy",
        "message": "Application is running successfully."
    })


@web_bp.route("/version", methods=["GET"])
def version():
    return jsonify({
        "application": "AI Career Intelligence Platform",
        "version": "1.0.0"
    })