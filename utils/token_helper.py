"""
=========================================================
AI Career Intelligence Platform
Password Reset Token Helper
=========================================================
"""

import secrets


def generate_reset_token() -> str:
    """
    Generate a secure password reset token.

    Returns:
        str: Random secure token.
    """

    return secrets.token_urlsafe(32)