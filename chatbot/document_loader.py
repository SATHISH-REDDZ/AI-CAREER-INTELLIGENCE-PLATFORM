"""
=========================================================
AI Career Intelligence Platform
Chatbot Document & Resume Loader
=========================================================
"""

from typing import Dict, Any
from services.pdf_service import PDFService


class ChatbotDocumentLoader:
    """
    Utility for loading and splitting uploaded documents (PDF/DOCX) into text chunks.
    """

    @staticmethod
    def load_document(filepath: str) -> Dict[str, Any]:
        text = PDFService.extract_text(filepath)
        word_count = len(text.split()) if text else 0
        return {
            "filepath": filepath,
            "text": text,
            "word_count": word_count,
            "success": bool(text)
        }
