"""
=========================================================
AI Career Intelligence Platform
Database Connection Manager
=========================================================

This module provides helper functions for managing
database connections and sessions.
=========================================================
"""

from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db


def get_session():
    """
    Return the current SQLAlchemy session.

    Returns:
        Session: Active SQLAlchemy session.
    """
    return db.session


def commit() -> bool:
    """
    Commit the current transaction.

    Returns:
        bool: True if commit succeeds, otherwise False.
    """
    try:
        db.session.commit()
        return True

    except SQLAlchemyError as error:
        print(f"Database Commit Error: {error}")
        db.session.rollback()
        return False


def rollback() -> None:
    """
    Roll back the current transaction.
    """
    db.session.rollback()


def close() -> None:
    """
    Close the current database session.
    """
    db.session.close()


def is_connected() -> bool:
    """
    Check whether the database connection is available.

    Returns:
        bool: True if connected.
    """
    try:
        db.session.execute(db.text("SELECT 1"))
        return True

    except SQLAlchemyError:
        return False


def execute_query(query: str, parameters: Optional[dict] = None):
    """
    Execute a raw SQL query.

    Args:
        query (str): SQL query.
        parameters (dict, optional): Query parameters.

    Returns:
        Result: SQLAlchemy execution result.
    """
    if parameters is None:
        parameters = {}

    return db.session.execute(
        db.text(query),
        parameters
    )