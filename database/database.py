"""
=========================================================
AI Career Intelligence Platform
Database Initialization
=========================================================

This module initializes and manages the application's
database using SQLAlchemy.
=========================================================
"""

from flask import Flask
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db

# ---------------------------------------------------------
# IMPORTANT:
# Import all models before db.create_all()
# ---------------------------------------------------------

import models


def initialize_database(app: Flask) -> None:
    """
    Initialize the database and create all tables.
    """

    with app.app_context():
        try:
            db.create_all()
            print("Database initialized successfully.")

        except SQLAlchemyError as error:
            print(f"Database initialization failed: {error}")


def get_database():
    """
    Return the SQLAlchemy database instance.
    """
    return db


def commit_session() -> bool:
    """
    Commit the current database session.
    """

    try:
        db.session.commit()
        return True

    except SQLAlchemyError:
        db.session.rollback()
        return False


def rollback_session() -> None:
    """
    Roll back the current database session.
    """
    db.session.rollback()


def close_session() -> None:
    """
    Close the current database session.
    """
    db.session.close()