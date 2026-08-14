"""
=========================================================
AI Career Intelligence Platform
Authentication Routes
=========================================================
"""

from flask import Blueprint

from controllers.auth_controller import AuthController
from utils.decorators import login_required

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register a new user.
    """
    return AuthController.register()


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User Login.
    """
    return AuthController.login()


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    """
    User Logout.
    """
    return AuthController.logout()


@auth_bp.route("/profile", methods=["GET"])
@login_required
def profile():
    """
    Get user profile.
    """
    from controllers.user_controller import UserController
    return UserController.profile()


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    """
    Forgot Password.
    """
    return AuthController.forgot_password()


@auth_bp.route("/reset-password", methods=["POST"])
def reset_password():
    """
    Reset Password.
    """
    return AuthController.reset_password()


@auth_bp.route("/send-verification", methods=["POST"])
def send_verification():
    """
    Send Email Verification Link.
    """
    return AuthController.send_verification_email()


@auth_bp.route("/verify-email", methods=["POST"])
def verify_email():
    """
    Verify Email.
    """
    return AuthController.verify_email()


@auth_bp.route("/google", methods=["GET"])
def google_login():
    """
    Google OAuth Login Endpoint.
    """
    return AuthController.google_login()