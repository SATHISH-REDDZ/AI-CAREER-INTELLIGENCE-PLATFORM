"""
=========================================================
AI Career Intelligence Platform
Admin Controller
=========================================================
"""

from flask import jsonify


class AdminController:
    """
    Admin Controller
    """

    @staticmethod
    def dashboard():
        """
        Admin Dashboard
        """

        return jsonify({
            "success": True,
            "message": "Welcome to the Admin Dashboard!",
            "data": {
                "module": "Role-Based Access Control (RBAC)",
                "status": "Working"
            }
        }), 200