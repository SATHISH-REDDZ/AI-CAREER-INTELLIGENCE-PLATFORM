"""
=========================================================
AI Career Intelligence Platform
Chatbot Repository
=========================================================
"""

from typing import List, Optional

from app.extensions import db
from models.conversation import Conversation


class ChatbotRepository:
    """
    Repository for Conversation model.
    """

    @staticmethod
    def create(conversation: Conversation) -> Conversation:
        db.session.add(conversation)
        db.session.commit()
        return conversation

    @staticmethod
    def get_by_id(conversation_id: int) -> Optional[Conversation]:
        return Conversation.query.get(conversation_id)

    @staticmethod
    def get_by_user(user_id: int) -> List[Conversation]:
        return (
            Conversation.query
            .filter_by(user_id=user_id)
            .order_by(Conversation.created_at.desc())
            .all()
        )

    @staticmethod
    def get_all() -> List[Conversation]:
        return Conversation.query.order_by(
            Conversation.created_at.desc()
        ).all()

    @staticmethod
    def update() -> bool:
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def delete(conversation: Conversation) -> bool:
        try:
            db.session.delete(conversation)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def count() -> int:
        return Conversation.query.count()