"""
=========================================================
AI Career Intelligence Platform
User Database Model
=========================================================

This module defines the application's User model.
=========================================================
"""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db
from database.models import BaseModel


class User(UserMixin, BaseModel):
    """
    User Model
    """

    __tablename__ = "users"

    # -----------------------------------------------------
    # Personal Information
    # -----------------------------------------------------

    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=True
    )

    profile_image = db.Column(
        db.String(255),
        nullable=True
    )

    # -----------------------------------------------------
    # Account Information
    # -----------------------------------------------------

    role = db.Column(
        db.String(30),
        default="user"
    )

    is_verified = db.Column(
        db.Boolean,
        default=False
    )

    verification_token = db.Column(
        db.String(255),
        nullable=True
    )

    last_login = db.Column(
        db.DateTime,
        nullable=True
    )

    # -----------------------------------------------------
    # Password Reset
    # -----------------------------------------------------

    reset_token = db.Column(
        db.String(255),
        nullable=True
    )

    reset_token_expiry = db.Column(
        db.DateTime,
        nullable=True
    )

    # -----------------------------------------------------
    # Relationships
    # -----------------------------------------------------

    resumes = db.relationship(
        "Resume",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    reports = db.relationship(
        "Report",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    conversations = db.relationship(
        "Conversation",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    notifications = db.relationship(
        "Notification",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # -----------------------------------------------------
    # Password Methods
    # -----------------------------------------------------

    def set_password(self, password: str):
        """
        Hash and store password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        """
        Verify password.
        """
        return check_password_hash(
            self.password_hash,
            password
        )

    # -----------------------------------------------------
    # Flask Login
    # -----------------------------------------------------

    def get_id(self):
        """
        Return user ID.
        """
        return str(self.id)

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self):
        """
        Convert user object to dictionary.
        """

        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "role": self.role,
            "is_verified": self.is_verified,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_active": self.is_active
        }

    # -----------------------------------------------------
    # String Representation
    # -----------------------------------------------------

    def __repr__(self):

        return (
            f"<User "
            f"id={self.id} "
            f"email='{self.email}' "
            f"role='{self.role}'>"
        )