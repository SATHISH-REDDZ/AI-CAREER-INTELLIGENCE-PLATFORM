"""
=========================================================
AI Career Intelligence Platform
Notification Routes
=========================================================
"""

from flask import Blueprint
from controllers.notification_controller import NotificationController
from utils.decorators import login_required

notification_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/api/notifications"
)


@notification_bp.route("", methods=["GET"])
@login_required
def get_user_notifications():
    return NotificationController.get_user_notifications()


@notification_bp.route("/<int:notification_id>/read", methods=["PUT", "POST"])
@login_required
def mark_as_read(notification_id):
    return NotificationController.mark_as_read(notification_id)
