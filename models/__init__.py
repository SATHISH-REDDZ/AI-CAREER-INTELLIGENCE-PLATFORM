"""
=========================================================
AI Career Intelligence Platform
Models Package
=========================================================

Import all database models so SQLAlchemy registers them.
=========================================================
"""

from .user import User
from .resume import Resume
from .job import Job
from .skill import Skill
from .report import Report
from .analytics import Analytics
from .interview import Interview
from .conversation import Conversation
from .notification import Notification

__all__ = [
    "User",
    "Resume",
    "Job",
    "Skill",
    "Report",
    "Analytics",
    "Interview",
    "Conversation",
    "Notification",
]