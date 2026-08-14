"""
=========================================================
AI Career Intelligence Platform
Chatbot Response Generator
=========================================================
"""

from typing import Dict, Any
from chatbot.prompts import get_persona_prompt
from services.chatbot_service import ChatbotService


class ResponseGenerator:
    """
    Generate conversational AI responses with persona selection and structured results.
    """

    @staticmethod
    def generate(
        user_id: int,
        query: str,
        persona: str = "Career Advisor",
        model: str = "Gemini",
        resume_text: str = ""
    ) -> Dict[str, Any]:
        """
        Generate answer using ChatbotService with selected persona and model.
        """
        result = ChatbotService.answer_query(
            user_id=user_id,
            query=query,
            model=model,
            persona=persona,
            resume_text=resume_text
        )
        return result
