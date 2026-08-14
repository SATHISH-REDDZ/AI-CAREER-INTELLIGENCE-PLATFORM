"""
=========================================================
AI Career Intelligence Platform
Chatbot History & Feedback Tracker
=========================================================
"""

from typing import Dict, Any, List
from app.extensions import db
from models.conversation import Conversation

_feedback_memory_db: List[Dict[str, Any]] = []


class ChatFeedback:
    """
    Record user feedback for chatbot responses in DB and memory.
    """

    @staticmethod
    def record_feedback(
        user_id: int,
        query: str = "",
        response: str = "",
        rating: int = 5,
        feedback_type: str = "thumbs_up",
        comment: str = "",
        conversation_id: int = None
    ) -> Dict[str, Any]:
        """
        Record feedback to database Conversation table and memory store.
        """
        entry = {
            "user_id": user_id,
            "conversation_id": conversation_id,
            "query": query,
            "response": response,
            "rating": rating,
            "feedback_type": feedback_type,
            "comment": comment
        }
        _feedback_memory_db.append(entry)

        # Update database conversation record if conversation_id provided
        if conversation_id:
            try:
                conv = Conversation.query.get(conversation_id)
                if conv:
                    conv.feedback = feedback_type
                    db.session.commit()
            except Exception as err:
                print("Error updating conversation feedback in DB:", err)

        return {"success": True, "message": "Feedback successfully recorded."}

    @staticmethod
    def get_all_feedback() -> List[Dict[str, Any]]:
        return _feedback_memory_db
