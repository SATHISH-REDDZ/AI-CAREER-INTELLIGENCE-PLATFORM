"""
=========================================================
AI Career Intelligence Platform
User Controller
=========================================================
"""

from flask import jsonify, g

from repositories.user_repository import UserRepository


class UserController:
    """
    User Controller
    """

    @staticmethod
    def profile():
        """
        Return logged-in user profile.
        """

        user = UserRepository.get_by_id(g.user_id)

        if user is None:
            return jsonify({
                "success": False,
                "message": "User not found."
            }), 404

        return jsonify({
            "success": True,
            "user": user.to_dict()
        }), 200