"""
=========================================================
AI Career Intelligence Platform
NLP Similarity Calculator
=========================================================
"""

import math
from collections import Counter


class SimilarityCalculator:
    """
    Calculate text similarity metrics.
    """

    @staticmethod
    def cosine_similarity(text1: str, text2: str) -> float:
        """
        Calculate TF cosine similarity between two text strings.
        """
        if not text1 or not text2:
            return 0.0

        words1 = [w.lower() for w in text1.split() if len(w) > 2]
        words2 = [w.lower() for w in text2.split() if len(w) > 2]

        vec1 = Counter(words1)
        vec2 = Counter(words2)

        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0

        return round(float(numerator) / denominator, 4)
