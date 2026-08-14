"""
=========================================================
AI Career Intelligence Platform
Chatbot Embeddings Helper
=========================================================
"""

from typing import List, Dict, Any
from rag.pipeline import VectorEmbeddings


class EmbeddingsHelper:
    """
    Generate vector embeddings for text tokens and queries.
    """

    @staticmethod
    def embed_text(text: str) -> Dict[str, float]:
        return VectorEmbeddings.get_embedding(text)
