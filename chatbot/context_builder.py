"""
=========================================================
AI Career Intelligence Platform
Chatbot Context Builder
=========================================================
"""

from typing import List, Dict, Any, Optional


class ContextBuilder:
    """
    Build multi-layered context combining RAG domain knowledge, user profile, resume snapshot, and chat history.
    """

    @staticmethod
    def build_context(
        user_id: int,
        query: str,
        resume_text: str = "",
        target_role: str = "",
        history: Optional[List[Dict[str, Any]]] = None
    ) -> str:
        context_parts = []

        # 1. RAG Domain Knowledge Context
        try:
            from rag.query_engine import RAGQueryEngine
            rag_context = RAGQueryEngine.query(query)
            if rag_context:
                context_parts.append(f"### Knowledge Base Context:\n{rag_context}")
        except Exception:
            pass

        # 2. Target Role
        if target_role:
            context_parts.append(f"### Candidate Target Role:\n{target_role}")

        # 3. Candidate Resume Context Snapshot
        if resume_text:
            cleaned_resume = resume_text[:1500].strip()
            context_parts.append(f"### Candidate Resume Snapshot:\n{cleaned_resume}")

        # 4. Recent Chat History Context
        if history:
            recent_turns = []
            for turn in history[-4:]:
                role_label = turn.get("role", "user").capitalize()
                content_text = turn.get("content", turn.get("answer", turn.get("question", "")))
                if content_text:
                    recent_turns.append(f"{role_label}: {content_text}")
            if recent_turns:
                context_parts.append("### Recent Conversation History:\n" + "\n".join(recent_turns))

        return "\n\n".join(context_parts)
