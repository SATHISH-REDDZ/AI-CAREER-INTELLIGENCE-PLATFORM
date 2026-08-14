"""
=========================================================
AI Career Intelligence Platform
RAG FAISS Vector Store Index Engine
=========================================================
"""

import numpy as np
from typing import List, Dict, Any
from nlp.similarity import SimilarityCalculator


class FAISSVectorIndex:
    """
    FAISS-backed Vector Store Index with dense L2/Cosine similarity search.
    """

    def __init__(self, dimension: int = 128):
        self.dimension = dimension
        self.chunks: List[Dict[str, Any]] = []
        self.index = None
        self._faiss_available = False

        try:
            import faiss
            self.index = faiss.IndexFlatL2(self.dimension)
            self._faiss_available = True
        except Exception:
            self._faiss_available = False

    def _text_to_vector(self, text: str) -> np.ndarray:
        vec = np.zeros(self.dimension, dtype=np.float32)
        if not text:
            return vec
        words = text.lower().split()
        for idx, word in enumerate(words):
            hash_val = sum(ord(c) for c in word) % self.dimension
            vec[hash_val] += 1.0
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm
        return vec

    def add_document(self, doc_id: str, title: str, text_content: str):
        from rag.document_loader import TextSplitter
        splits = TextSplitter.split_text(text_content)

        vectors = []
        for idx, chunk_text in enumerate(splits):
            vec = self._text_to_vector(chunk_text)
            vectors.append(vec)
            self.chunks.append({
                "doc_id": doc_id,
                "title": title,
                "chunk_id": idx,
                "content": chunk_text,
                "vector": vec
            })

        if self._faiss_available and self.index and vectors:
            mat = np.vstack(vectors).astype(np.float32)
            self.index.add(mat)

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if not query or not self.chunks:
            return []

        # 1. FAISS Search if available
        if self._faiss_available and self.index and self.index.ntotal > 0:
            try:
                q_vec = np.expand_dims(self._text_to_vector(query), axis=0).astype(np.float32)
                distances, indices = self.index.search(q_vec, min(top_k, len(self.chunks)))
                results = []
                for dist, idx in zip(distances[0], indices[0]):
                    if idx >= 0 and idx < len(self.chunks):
                        chunk = self.chunks[idx]
                        score = max(0.0, 1.0 - float(dist))
                        results.append({
                            "score": score,
                            "title": chunk["title"],
                            "content": chunk["content"]
                        })
                return results
            except Exception as err:
                print(f"[FAISSVectorIndex] FAISS search error: {err}")

        # 2. Pure Cosine Similarity Fallback
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


class VectorStoreIndex(FAISSVectorIndex):
    """
    Backward-compatible VectorStoreIndex wrapper.
    """
    pass


class RAGPipeline:
    """
    End-to-End FAISS RAG Pipeline for Career Chatbot.
    """

    def __init__(self):
        self.index = VectorStoreIndex(dimension=128)
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
