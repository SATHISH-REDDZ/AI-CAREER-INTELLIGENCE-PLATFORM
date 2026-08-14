"""
=========================================================
AI Career Intelligence Platform
Chatbot Session Manager
=========================================================
"""

from typing import Dict, Any, Optional
from chatbot.conversation import ChatSession

_active_sessions: Dict[str, ChatSession] = {}


class SessionManager:
    """
    Manages active chatbot sessions across users.
    """

    @classmethod
    def get_or_create_session(cls, session_id: str, user_id: int) -> ChatSession:
        if session_id not in _active_sessions:
            _active_sessions[session_id] = ChatSession(session_id, user_id)
        return _active_sessions[session_id]

    @classmethod
    def reset_session(cls, user_id: int) -> Dict[str, Any]:
        from chatbot.chatbot import CareerChatbotEngine
        memory = CareerChatbotEngine.get_memory(user_id)
        memory.clear()
        return {"success": True, "message": "Session reset successfully."}
