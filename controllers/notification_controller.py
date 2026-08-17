"""
=========================================================
AI Career Intelligence Platform
Notification Controller
=========================================================
"""

from flask import jsonify, request, g
from services.notification_service import NotificationService
from utils.decorators import login_required


class NotificationController:
    """
    Notification Controller handling user in-app notifications.
    """

    @staticmethod
    def get_user_notifications():
        user_id = getattr(g, "user_id", 1)
        notifications = NotificationService.get_user_notifications(user_id)
        return jsonify({
            "success": True,
            "notifications": notifications
        }), 200

    @staticmethod
    def mark_as_read(notification_id: int):
        user_id = getattr(g, "user_id", 1)
        result = NotificationService.mark_as_read(notification_id=notification_id, user_id=user_id)
        return jsonify(result), 200
