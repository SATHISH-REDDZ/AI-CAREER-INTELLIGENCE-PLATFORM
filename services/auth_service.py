"""
=========================================================
AI Career Intelligence Platform
Authentication Service
=========================================================
"""

from datetime import datetime, timedelta

from models.user import User
from repositories.user_repository import UserRepository
from utils.jwt_helper import generate_token
from utils.token_helper import generate_reset_token
from utils.validators import (
    is_valid_email,
    is_strong_password,
)


class AuthService:
    """
    Authentication Business Logic
    """

    @staticmethod
    def register(full_name: str, email: str, password: str):
        """
        Register a new user.
        """

        if not is_valid_email(email):
            return False, "Invalid email address."

        if not is_strong_password(password):
            return False, "Password is not strong enough."

        if UserRepository.exists(email):
            return False, "Email already exists."

        user = User(
            full_name=full_name,
            email=email
        )

        user.set_password(password)

        UserRepository.create(user)

        return True, "User registered successfully."

    @staticmethod
    def login(email: str, password: str):
        """
        Authenticate a user.
        """

        user = UserRepository.get_by_email(email)

        if user is None:
            return False, "User not found."

        if not user.check_password(password):
            return False, "Invalid password."

        token = generate_token(user.id)

        return True, {
            "token": token,
            "user": user.to_dict()
        }

    @staticmethod
    def logout():
        """
        Logout user.
        """

        return True, "Logged out successfully."

    @staticmethod
    def forgot_password(email: str):
        """
        Generate password reset token.
        """

        user = UserRepository.get_by_email(email)

        if user is None:
            return False, "User not found."

        reset_token = generate_reset_token()

        # SQLite stores naive datetimes
        expiry = datetime.now() + timedelta(minutes=30)

        UserRepository.save_reset_token(
            user,
            reset_token,
            expiry
        )

        # Temporary: print reset link
        print("\n===================================")
        print("PASSWORD RESET LINK")
        print("http://127.0.0.1:5000/reset-password")
        print(f"Token: {reset_token}")
        print("===================================\n")

        return True, (
            "Password reset link generated successfully. "
            "Check the server console."
        )

    @staticmethod
    def reset_password(token: str, new_password: str):
        """
        Reset user password using reset token.
        """

        user = UserRepository.get_by_reset_token(token)

        if user is None:
            return False, "Invalid reset token."

        if user.reset_token_expiry is None:
            return False, "Reset token has expired."

        current_time = datetime.now()

        if current_time > user.reset_token_expiry:
            return False, "Reset token has expired."

        if not is_strong_password(new_password):
            return False, "Password is not strong enough."

        user.set_password(new_password)
        UserRepository.clear_reset_token(user)
        UserRepository.update(user)

        return True, "Password reset successfully."

    @staticmethod
    def send_verification_email(email: str):
        """
        Generate email verification token.
        """

        user = UserRepository.get_by_email(email)

        if user is None:
            return False, "User not found."

        if user.is_verified:
            return False, "Email is already verified."

        verification_token = generate_reset_token()

        UserRepository.save_verification_token(
            user,
            verification_token
        )

        print("\n===================================")
        print("EMAIL VERIFICATION LINK")
        print("http://127.0.0.1:5000/verify-email")
        print(f"Token: {verification_token}")
        print("===================================\n")

        return True, (
            "Verification link generated successfully. "
            "Check the server console."
        )

    @staticmethod
    def verify_email(token: str):
        """
        Verify user email.
        """

        user = UserRepository.get_by_verification_token(token)

        if user is None:
            return False, "Invalid verification token."

        UserRepository.verify_user(user)

        return True, "Email verified successfully."