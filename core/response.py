"""
=========================================================
AI Career Intelligence Platform
API Response Helper
=========================================================
"""

from flask import jsonify


def success_response(data=None, message: str = "Operation successful", status_code: int = 200):
    """
    Format standard successful API response.
    """
    payload = {
        "success": True,
        "message": message
    }
    if data is not None:
        payload["data"] = data

    return jsonify(payload), status_code


def error_response(message: str = "An error occurred", status_code: int = 400, errors=None):
    """
    Format standard error API response.
    """
    payload = {
        "success": False,
        "message": message
    }
    if errors is not None:
        payload["errors"] = errors

    return jsonify(payload), status_code
