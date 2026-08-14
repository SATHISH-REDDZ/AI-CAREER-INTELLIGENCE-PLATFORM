"""
=========================================================
AI Career Intelligence Platform
JWT Helper
=========================================================

Utility functions for JWT token generation and validation.
=========================================================
"""

from datetime import datetime, timedelta, UTC

import jwt
from flask import current_app


def generate_token(user_id: int) -> str:
    """
    Generate a JWT token.

    Args:
        user_id (int): User ID.

    Returns:
        str: JWT token.
    """

    payload = {
        "user_id": user_id,
        "exp": datetime.now(UTC) + timedelta(hours=24),
        "iat": datetime.now(UTC)
    }

    token = jwt.encode(
        payload,
        current_app.config["JWT_SECRET_KEY"],
        algorithm="HS256"
    )

    return token


def decode_token(token: str):
    """
    Decode a JWT token.

    Args:
        token (str): JWT token.

    Returns:
        dict | None
    """

    try:
        payload = jwt.decode(
            token,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=["HS256"]
        )
        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None


def verify_token(token: str) -> bool:
    """
    Verify whether a JWT token is valid.

    Args:
        token (str): JWT token.

    Returns:
        bool
    """

    return decode_token(token) is not None