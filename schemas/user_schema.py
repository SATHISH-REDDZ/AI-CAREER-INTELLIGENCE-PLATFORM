"""
=========================================================
AI Career Intelligence Platform
User Schema Validator
=========================================================
"""


class UserSchema:

    REQUIRED_FIELDS = [
        "full_name",
        "email",
        "password"
    ]

    @staticmethod
    def validate_register(data: dict) -> tuple[bool, str]:
        if not data:
            return False, "Request body is empty."

        for field in UserSchema.REQUIRED_FIELDS:
            if not data.get(field):
                return False, f"Missing required field: '{field}'."

        email = data.get("email", "").strip()
        if "@" not in email or "." not in email:
            return False, "Invalid email address format."

        password = data.get("password", "")
        if len(password) < 6:
            return False, "Password must be at least 6 characters long."

        return True, ""

    @staticmethod
    def validate_login(data: dict) -> tuple[bool, str]:
        if not data:
            return False, "Request body is empty."

        if not data.get("email") or not data.get("password"):
            return False, "Both email and password are required."

        return True, ""