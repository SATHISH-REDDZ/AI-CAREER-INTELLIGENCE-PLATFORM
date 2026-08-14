"""
=========================================================
AI Career Intelligence Platform
User Service
=========================================================
"""

from repositories.user_repository import UserRepository


class UserService:
    """
    User management business logic.
    """

    @staticmethod
    def get_user(user_id: int):
        """
        Get user by ID.
        """
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def get_all_users():
        """
        Return all users.
        """
        return UserRepository.get_all()

    @staticmethod
    def delete_user(user_id: int):
        """
        Delete user.
        """

        user = UserRepository.get_by_id(user_id)

        if user is None:
            return False

        return UserRepository.delete(user)

    @staticmethod
    def update_user():
        """
        Save pending user changes.
        """
        return UserRepository.update()