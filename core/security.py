"""
=========================================================
AI Career Intelligence Platform
Core Security Utilities
=========================================================
"""

import html


def sanitize_input(text: str) -> str:
    """
    Sanitize raw user input text against XSS attacks.
    """
    if not text:
        return ""
    return html.escape(text.strip())
