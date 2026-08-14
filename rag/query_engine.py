"""
=========================================================
AI Career Intelligence Platform
RAG Query Engine
=========================================================
"""
from rag.pipeline import RAGPipeline

query_engine_instance = RAGPipeline()


class RAGQueryEngine:
    @staticmethod
    def query(user_query: str) -> str:
        return query_engine_instance.retrieve_context(user_query)
