"""
=========================================================
AI Career Intelligence Platform
Authentication Decorators
=========================================================
"""

from functools import wraps

from flask import jsonify, request, g

from app.extensions import db
from models.user import User
from utils.jwt_helper import decode_token


def login_required(func):
    """
    JWT Authentication Decorator.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({
                "success": False,
                "message": "Authorization token is missing."
            }), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({
                "success": False,
                "message": "Invalid authorization header."
            }), 401

        token = auth_header.split(" ")[1]

        payload = decode_token(token)

        if payload is None:
            return jsonify({
                "success": False,
                "message": "Invalid or expired token."
            }), 401

        user = db.session.get(User, payload["user_id"])

        if user is None:
            return jsonify({
                "success": False,
                "message": "User not found."
            }), 404

        g.user_id = user.id
        g.current_user = user

        return func(*args, **kwargs)

    return wrapper


def roles_required(*roles):
    """
    Role-Based Authorization Decorator.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            current_user = getattr(g, "current_user", None)

            if current_user is None:
                return jsonify({
                    "success": False,
                    "message": "Unauthorized."
                }), 401

            if current_user.role not in roles:
                return jsonify({
                    "success": False,
                    "message": "Access denied."
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator