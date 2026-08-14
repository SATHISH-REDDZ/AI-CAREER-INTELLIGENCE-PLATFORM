"""
=========================================================
AI Career Intelligence Platform
PDF & Document Text Extraction Service
=========================================================
"""

import os
from pathlib import Path


class PDFService:
    """
    Service for extracting text from PDF and DOCX documents.
    """

    @staticmethod
    def extract_text_from_pdf(filepath: str) -> str:
        """
        Extract plain text from a PDF file.
        """
        text = ""

        # Try pypdf / PyPDF2
        try:
            from pypdf import PdfReader
            reader = PdfReader(filepath)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            if text.strip():
                return text.strip()
        except Exception:
            pass

        try:
            import pdfplumber
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
            if text.strip():
                return text.strip()
        except Exception:
            pass

        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(filepath)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            if text.strip():
                return text.strip()
        except Exception:
            pass

        return text.strip()

    @staticmethod
    def extract_text_from_docx(filepath: str) -> str:
        """
        Extract plain text from a DOCX file.
        """
        text = ""
        try:
            import docx
            doc = docx.Document(filepath)
            paragraphs = [p.text for p in doc.paragraphs if p.text]
            text = "\n".join(paragraphs)
            if text.strip():
                return text.strip()
        except Exception:
            pass

        # Native zipfile XML fallback for DOCX text extraction
        try:
            import re
            import zipfile
            with zipfile.ZipFile(filepath) as z:
                xml_content = z.read("word/document.xml").decode("utf-8", errors="ignore")
                # Remove XML tags to extract inner text
                text = re.sub(r"<[^>]+>", " ", xml_content)
                text = re.sub(r"\s+", " ", text).strip()
        except Exception:
            pass

        return text.strip()

    @classmethod
    def extract_text(cls, filepath: str) -> str:
        """
        Extract text based on file extension.
        """
        if not os.path.exists(filepath):
            return ""

        ext = Path(filepath).suffix.lower()

        if ext == ".pdf":
            text = cls.extract_text_from_pdf(filepath)
        elif ext in (".docx", ".doc"):
            text = cls.extract_text_from_docx(filepath)

        if not text:
            # Fallback to reading file directly as plain text if possible
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            except Exception:
                pass

        return text.strip()
