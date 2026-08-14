"""
=========================================================
AI Career Intelligence Platform
NLP Text Cleaner
=========================================================
"""

import re
import string


class TextCleaner:
    """
    Clean and normalize plain text extracted from resumes & documents.
    """

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Remove non-printable / unicode noise
        cleaned = re.sub(r"[^\x00-\x7F]+", " ", text)
        # Replace multiple spaces/newlines with single whitespace
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned.strip()

    @staticmethod
    def to_lower(text: str) -> str:
        return TextCleaner.clean(text).lower()

    @staticmethod
    def remove_punctuation(text: str) -> str:
        cleaned = TextCleaner.clean(text)
        return cleaned.translate(str.maketrans("", "", string.punctuation))
