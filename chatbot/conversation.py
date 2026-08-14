"""
=========================================================
AI Career Intelligence Platform
Chatbot Conversation Session Manager
=========================================================
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


class ChatSession:
    """
    Represents an active multi-turn conversational session.
    """

    def __init__(self, session_id: str, user_id: int):
        self.session_id = session_id
        self.user_id = user_id
        self.created_at = datetime.utcnow()
        self.active_resume: Optional[str] = None
        self.target_role: Optional[str] = None
        self.persona: str = "Career Advisor"
        self.messages: List[Dict[str, Any]] = []

    def add_turn(self, question: str, answer: str, meta: Dict[str, Any] = None):
        turn = {
            "question": question,
            "answer": answer,
            "timestamp": datetime.utcnow().isoformat()
        }
        if meta:
            turn.update(meta)
        self.messages.append(turn)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "persona": self.persona,
            "active_resume": bool(self.active_resume),
            "turn_count": len(self.messages),
            "created_at": self.created_at.isoformat()
        }
