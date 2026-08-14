"""
=========================================================
AI Career Intelligence Platform
Core Exceptions
=========================================================
"""


class AppException(Exception):
    """Base exception for application errors."""
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class ValidationError(AppException):
    """Validation exception."""
    def __init__(self, message: str = "Invalid input parameters."):
        super().__init__(message, status_code=400)


class AuthenticationError(AppException):
    """Authentication exception."""
    def __init__(self, message: str = "Authentication failed."):
        super().__init__(message, status_code=401)


class NotFoundError(AppException):
    """Resource not found exception."""
    def __init__(self, message: str = "Requested resource not found."):
        super().__init__(message, status_code=404)
