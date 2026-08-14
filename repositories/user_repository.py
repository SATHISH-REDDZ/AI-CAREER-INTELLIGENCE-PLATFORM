"""
=========================================================
AI Career Intelligence Platform
User Repository
=========================================================
"""

from datetime import datetime

from app.extensions import db
from models.user import User


class UserRepository:
    """
    User Repository
    """

    @staticmethod
    def create(user: User):
        """
        Create a new user.
        """
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_email(email: str):
        """
        Get user by email.
        """
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id: int):
        """
        Get user by ID.
        """
        return User.query.get(user_id)

    @staticmethod
    def exists(email: str) -> bool:
        """
        Check if email already exists.
        """
        return User.query.filter_by(email=email).first() is not None

    @staticmethod
    def save_reset_token(user: User, token: str, expiry: datetime):
        """
        Save password reset token.
        """
        user.reset_token = token
        user.reset_token_expiry = expiry

        db.session.commit()

    @staticmethod
    def get_by_reset_token(token: str):
        """
        Find user using reset token.
        """
        return User.query.filter_by(
            reset_token=token
        ).first()

    @staticmethod
    def clear_reset_token(user: User):
        """
        Remove reset token after password reset.
        """
        user.reset_token = None
        user.reset_token_expiry = None

        db.session.commit()

    @staticmethod
    def update(user: User):
        """
        Save user changes.
        """
        db.session.commit()

    @staticmethod
    def save_verification_token(user: User, token: str):
        """
        Save email verification token.
        """
        user.verification_token = token
        db.session.commit()

    @staticmethod
    def get_by_verification_token(token: str):
        """
        Find user by verification token.
        """
        return User.query.filter_by(
            verification_token=token
        ).first()

    @staticmethod
    def verify_user(user: User):
        """
        Verify user account.
        """
        user.is_verified = True
        user.verification_token = None
        db.session.commit()