"""
=========================================================
AI Career Intelligence Platform
Authentication Controller
=========================================================
"""

from flask import jsonify, request

from services.auth_service import AuthService


class AuthController:
    """
    Authentication Controller
    """

    @staticmethod
    def register():
        """
        Register a new user.
        """

        data = request.get_json()

        success, result = AuthService.register(
            full_name=data.get("full_name"),
            email=data.get("email"),
            password=data.get("password")
        )

        if success:
            return jsonify({
                "success": True,
                "message": result
            }), 201

        return jsonify({
            "success": False,
            "message": result
        }), 400

    @staticmethod
    def login():
        """
        User Login
        """

        data = request.get_json()

        success, result = AuthService.login(
            email=data.get("email"),
            password=data.get("password")
        )

        if success:
            return jsonify({
                "success": True,
                "token": result["token"]
            }), 200

        return jsonify({
            "success": False,
            "message": result
        }), 401

    @staticmethod
    def logout():
        """
        User Logout
        """

        success, message = AuthService.logout()

        if success:
            return jsonify({
                "success": True,
                "message": message
            }), 200

        return jsonify({
            "success": False,
            "message": message
        }), 400

    @staticmethod
    def forgot_password():
        """
        Forgot Password
        """

        data = request.get_json()

        success, message = AuthService.forgot_password(
            data.get("email")
        )

        if success:
            return jsonify({
                "success": True,
                "message": message
            }), 200

        return jsonify({
            "success": False,
            "message": message
        }), 400

    @staticmethod
    def reset_password():
        """
        Reset Password
        """

        data = request.get_json()

        success, message = AuthService.reset_password(
            token=data.get("token"),
            new_password=data.get("new_password")
        )

        if success:
            return jsonify({
                "success": True,
                "message": message
            }), 200

        return jsonify({
            "success": False,
            "message": message
        }), 400

    @staticmethod
    def send_verification_email():
        """
        Send Email Verification Link
        """

        data = request.get_json()

        success, message = AuthService.send_verification_email(
            data.get("email")
        )

        if success:
            return jsonify({
                "success": True,
                "message": message
            }), 200

        return jsonify({
            "success": False,
            "message": message
        }), 400

    @staticmethod
    def verify_email():
        """
        Verify Email
        """

        data = request.get_json()

        success, message = AuthService.verify_email(
            data.get("token")
        )

        if success:
            return jsonify({
                "success": True,
                "message": message
            }), 200

        return jsonify({
            "success": False,
            "message": message
        }), 400

    @staticmethod
    def google_login():
        """
        Google OAuth Login Redirect
        """
        return jsonify({
            "success": True,
            "oauth_url": "https://accounts.google.com/o/oauth2/v2/auth?client_id=demo_client_id&response_type=code&scope=openid%20email%20profile&redirect_uri=http://127.0.0.1:5000/api/auth/google/callback"
        }), 200