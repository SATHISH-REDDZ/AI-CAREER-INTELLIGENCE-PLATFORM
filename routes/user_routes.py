"""
=========================================================
AI Career Intelligence Platform
User Routes
=========================================================
"""

from flask import Blueprint

from controllers.user_controller import UserController
from utils.decorators import login_required

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/api/user"
)


@user_bp.route("/profile", methods=["GET"])
@login_required
def profile():
    """
    Logged-in user profile.
    """
    return UserController.profile()