"""
=========================================================
AI Career Intelligence Platform
Application Logging Configuration
=========================================================

This module configures centralized logging for the
entire application.
=========================================================
"""

import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging() -> logging.Logger:
    """
    Configure and return the application logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    # -----------------------------------------------------
    # Create logs directory
    # -----------------------------------------------------

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("AICareerPlatform")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # -----------------------------------------------------
    # Log Format
    # -----------------------------------------------------

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # -----------------------------------------------------
    # Console Handler
    # -----------------------------------------------------

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # -----------------------------------------------------
    # Application Log File
    # -----------------------------------------------------

    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    # -----------------------------------------------------
    # Add Handlers
    # -----------------------------------------------------

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("Logging system initialized successfully.")

    return logger