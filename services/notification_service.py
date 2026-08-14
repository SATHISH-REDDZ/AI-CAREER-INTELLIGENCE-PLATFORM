"""
=========================================================
AI Career Intelligence Platform
Notification Service
=========================================================
"""


class NotificationService:
    """
    Notifications System Business Logic
    """

    @staticmethod
    def get_user_notifications(user_id: int) -> dict:
        """
        Get candidate notifications and alerts.
        """
        notifications = [
            {
                "id": 1,
                "title": "Resume Parsed Successfully",
                "message": "Your uploaded resume has been analyzed with an ATS score of 80.5/100.",
                "type": "info",
                "read": False
            },
            {
                "id": 2,
                "title": "New Job Match Found",
                "message": "3 new roles matching your Python and Flask skills are available.",
                "type": "job_alert",
                "read": False
            }
        ]

        return {
            "success": True,
            "notifications": notifications
        }
