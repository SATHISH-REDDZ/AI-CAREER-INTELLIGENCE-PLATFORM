"""
=========================================================
AI Career Intelligence Platform
RAG Embeddings & Vector Index Engine
=========================================================
"""

import math
from collections import Counter
from typing import List, Dict, Any
from nlp.similarity import SimilarityCalculator


class VectorEmbeddings:
    """
    Sentence and Document Vector Generator (TF-IDF representation).
    """

    @staticmethod
    def get_embedding(text: str) -> Dict[str, float]:
        if not text:
            return {}
        words = [w.lower() for w in text.split() if len(w) > 2]
        total = max(len(words), 1)
        counts = Counter(words)
        return {w: c / total for w, c in counts.items()}


class VectorStoreIndex:
    """
    Lightweight in-memory vector index manager for document chunks.
    """

    def __init__(self):
        self.chunks: List[Dict[str, Any]] = []

    def add_document(self, doc_id: str, title: str, text_content: str):
        from rag.document_loader import TextSplitter
        splits = TextSplitter.split_text(text_content)
        for idx, chunk_text in enumerate(splits):
            self.chunks.append({
                "doc_id": doc_id,
                "title": title,
                "chunk_id": idx,
                "content": chunk_text,
                "embedding": VectorEmbeddings.get_embedding(chunk_text)
            })

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if not query or not self.chunks:
            return []

        results = []
        for chunk in self.chunks:
            score = SimilarityCalculator.cosine_similarity(query, chunk["content"])
            if score > 0.05:
                results.append({
                    "score": score,
                    "title": chunk["title"],
                    "content": chunk["content"]
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]


class RAGPipeline:
    """
    End-to-End RAG Pipeline for Career Chatbot.
    """

    def __init__(self):
        self.index = VectorStoreIndex()
        self._seed_career_knowledge()

    def _seed_career_knowledge(self):
        self.index.add_document(
            "ats_guide",
            "ATS Optimization Best Practices",
            "To maximize ATS compatibility, use clean 1-column layouts, standard headers like Experience, Education, Skills, and exact keyword matches from the job description."
        )
        self.index.add_document(
            "interview_guide",
            "Technical Interview Preparation Strategy",
            "Structure behavioral questions with the STAR method (Situation, Task, Action, Result). For coding problems, outline your approach and time complexity before writing code."
        )
        self.index.add_document(
            "resume_guide",
            "Action Verb Resume Engineering",
            "Lead bullet points with high-impact action verbs like Architected, Engineered, Spearedheaded, Optimized, and Streamlined. Always include percentage or revenue metrics."
        )

    def retrieve_context(self, query: str, top_k: int = 2) -> str:
        matches = self.index.search(query, top_k=top_k)
        if not matches:
            return ""

        context_blocks = []
        for match in matches:
            context_blocks.append(f"[{match['title']}]: {match['content']}")

        return "\n\n".join(context_blocks)
