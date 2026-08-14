"""
=========================================================
AI Career Intelligence Platform
Admin Routes
=========================================================
"""

from flask import Blueprint

from controllers.admin_controller import AdminController
from utils.decorators import login_required, roles_required

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)


@admin_bp.route("/dashboard", methods=["GET"])
@login_required
@roles_required("admin")
def dashboard():
    """
    Admin Dashboard
    """
    return AdminController.dashboard()