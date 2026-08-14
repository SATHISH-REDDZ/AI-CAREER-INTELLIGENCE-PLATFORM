"""
=========================================================
AI Career Intelligence Platform
Main Conversational AI Chatbot Engine
=========================================================
"""

import time
from typing import Dict, Any, Optional
from chatbot.memory import ChatMemory
from chatbot.context_builder import ContextBuilder
from services.chatbot_service import ChatbotService
from app.extensions import db
from models.conversation import Conversation

_user_memories: Dict[int, ChatMemory] = {}


class CareerChatbotEngine:
    """
    Main Chatbot Coordinator managing memory, context building, database persistence, and service execution.
    """

    @classmethod
    def get_memory(cls, user_id: int) -> ChatMemory:
        if user_id not in _user_memories:
            _user_memories[user_id] = ChatMemory()
        return _user_memories[user_id]

    @classmethod
    def ask(
        cls,
        user_id: int,
        query: str,
        resume_text: str = "",
        model: str = "Gemini",
        persona: str = "Career Advisor",
        target_role: str = ""
    ) -> Dict[str, Any]:
        start_time = time.time()
        memory = cls.get_memory(user_id)
        history = memory.get_history()

        # Build context from RAG, resume, target role, and recent turns
        context = ContextBuilder.build_context(
            user_id=user_id,
            query=query,
            resume_text=resume_text,
            target_role=target_role,
            history=history
        )

        # Call service engine
        res = ChatbotService.answer_query(
            user_id=user_id,
            query=query,
            context=context,
            model=model,
            persona=persona,
            resume_text=resume_text
        )

        response_text = res.get("response", "Focus on technical fundamentals and project delivery.")
        suggestions = res.get("suggestions", [])
        html_embed = res.get("html_embed", "")
        tokens_used = res.get("tokens_used", len(query.split()) + len(response_text.split()))

        elapsed_seconds = round(time.time() - start_time, 3)

        # Update memory
        memory.add_message("user", query)
        memory.add_message("assistant", response_text)

        # Persist conversation entry to database if user is logged in
        conversation_id: Optional[int] = None
        try:
            conv = Conversation(
                user_id=user_id if user_id and user_id > 0 else 1,
                question=query,
                answer=response_text,
                conversation_type=persona,
                response_time=elapsed_seconds,
                tokens_used=tokens_used,
                ai_model=model
            )
            db.session.add(conv)
            db.session.commit()
            conversation_id = conv.id
        except Exception as err:
            db.session.rollback()
            print("Error persisting conversation to database:", err)

        return {
            "success": True,
            "conversation_id": conversation_id,
            "query": query,
            "response": response_text,
            "html_embed": html_embed,
            "suggestions": suggestions,
            "model": model,
            "persona": persona,
            "response_time": elapsed_seconds,
            "tokens_used": tokens_used,
            "history": memory.get_history()
        }
