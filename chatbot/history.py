"""
=========================================================
AI Career Intelligence Platform
Chatbot History Service
=========================================================
"""

from typing import List, Dict, Any
from models.conversation import Conversation


class ChatHistoryManager:
    """
    Manage fetching and filtering stored user conversation history.
    """

    @staticmethod
    def get_user_conversations(user_id: int, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Fetch conversation history entries for a given user.
        """
        try:
            records = (
                Conversation.query.filter_by(user_id=user_id)
                .order_by(Conversation.created_at.desc())
                .limit(limit)
                .all()
            )
            return [rec.to_dict() for rec in reversed(records)]
        except Exception as err:
            print("Error loading conversation history:", err)
            return []

    @staticmethod
    def clear_user_conversations(user_id: int) -> bool:
        """
        Clear memory for user session.
        """
        from chatbot.chatbot import CareerChatbotEngine
        memory = CareerChatbotEngine.get_memory(user_id)
        memory.clear()
        return True
