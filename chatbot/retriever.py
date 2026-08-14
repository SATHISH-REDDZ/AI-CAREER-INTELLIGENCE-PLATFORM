"""
=========================================================
AI Career Intelligence Platform
Chatbot RAG Retriever
=========================================================
"""

from typing import List, Dict, Any
from rag.query_engine import RAGQueryEngine


class ChatbotRetriever:
    """
    RAG context retriever for chatbot queries.
    """

    @staticmethod
    def retrieve(query: str, top_k: int = 3) -> str:
        return RAGQueryEngine.query(query)
