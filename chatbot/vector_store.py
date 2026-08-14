"""
=========================================================
AI Career Intelligence Platform
Chatbot Vector Store Manager
=========================================================
"""

from rag.pipeline import VectorStoreIndex


class ChatbotVectorStore:
    """
    In-memory vector store index for chatbot retrieval.
    """

    def __init__(self):
        self.index = VectorStoreIndex()

    def add_text(self, doc_id: str, title: str, content: str):
        self.index.add_document(doc_id, title, content)

    def search(self, query: str, top_k: int = 3):
        return self.index.search(query, top_k=top_k)
