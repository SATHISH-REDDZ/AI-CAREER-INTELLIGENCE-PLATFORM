"""
=========================================================
AI Career Intelligence Platform
Conversation Model
=========================================================
"""

from app.extensions import db
from database.models import BaseModel


class Conversation(BaseModel):
    """
    AI Chatbot Conversation Model
    """

    __tablename__ = "conversations"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    question = db.Column(
        db.Text,
        nullable=False
    )

    answer = db.Column(
        db.Text,
        nullable=False
    )

    conversation_type = db.Column(
        db.String(100),
        default="Career Guidance"
    )

    response_time = db.Column(
        db.Float,
        default=0.0
    )

    tokens_used = db.Column(
        db.Integer,
        default=0
    )

    ai_model = db.Column(
        db.String(100),
        default="Gemini"
    )

    feedback = db.Column(
        db.String(50),
        nullable=True
    )

    is_favorite = db.Column(
        db.Boolean,
        default=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "conversation_type": self.conversation_type,
            "response_time": self.response_time,
            "tokens_used": self.tokens_used,
            "ai_model": self.ai_model,
            "is_favorite": self.is_favorite
        }

    def __repr__(self):
        return f"<Conversation {self.id}>"