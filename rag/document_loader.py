"""
=========================================================
AI Career Intelligence Platform
RAG Document Loader & Text Chunker
=========================================================
"""

import os
from typing import List, Dict, Any


class DocumentLoader:
    """
    Load text and markdown career documents.
    """

    @staticmethod
    def load_from_directory(directory_path: str) -> List[Dict[str, str]]:
        documents = []
        if not os.path.exists(directory_path):
            return documents

        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith((".txt", ".md")):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            text = f.read()
                            documents.append({
                                "source": file,
                                "filepath": filepath,
                                "content": text
                            })
                    except Exception as err:
                        print(f"[DocumentLoader] Error reading {file}: {err}")
        return documents


class TextSplitter:
    """
    Split long documents into semantic chunks.
    """

    @staticmethod
    def split_text(text: str, chunk_size: int = 400, overlap: int = 50) -> List[str]:
        if not text:
            return []

        words = text.split()
        chunks = []
        i = 0
        while i < len(words):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
            i += (chunk_size - overlap)
        return chunks
