"""
=========================================================
AI Career Intelligence Platform
Database Seed Script
=========================================================
"""

from app.extensions import db
from models.user import User


def seed_database():
    """
    Insert initial data into the database.
    """

    if User.query.count() == 0:

        admin = User(
            full_name="Administrator",
            email="admin@careerai.com",
            password="admin123",
            role="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Default administrator created.")

    else:

        print("Database already seeded.")