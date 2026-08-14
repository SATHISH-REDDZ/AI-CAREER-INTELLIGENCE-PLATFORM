"""
=========================================================
AI Career Intelligence Platform
NLP Subsystem Modules
=========================================================
"""

import re
from typing import List, Dict, Any, Set
from collections import Counter
from nlp.text_cleaner import TextCleaner
from nlp.similarity import SimilarityCalculator

ENGLISH_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "because", "as", "what", "which",
    "this", "that", "these", "those", "then", "just", "so", "than", "such", "both",
    "through", "about", "against", "between", "into", "throughout", "during", "before",
    "after", "above", "below", "to", "from", "up", "upon", "down", "in", "out", "on",
    "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "can", "will", "just", "should", "now", "i", "me", "my", "myself", "we", "our", "ours",
    "you", "your", "yours", "he", "him", "his", "she", "her", "hers", "it", "its", "they",
    "them", "their", "theirs", "is", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing", "for", "with", "by", "at"
}


class Stopwords:
    @staticmethod
    def get_stopwords() -> Set[str]:
        return ENGLISH_STOPWORDS


class Tokenizer:
    @staticmethod
    def tokenize(text: str) -> List[str]:
        if not text:
            return []
        tokens = re.findall(r"\b\w+\b", text.lower())
        return [t for t in tokens if t not in ENGLISH_STOPWORDS and len(t) > 1]


class KeywordMatcher:
    @staticmethod
    def match(source_text: str, target_text: str) -> Dict[str, Any]:
        source_tokens = set(Tokenizer.tokenize(source_text))
        target_tokens = set(Tokenizer.tokenize(target_text))

        matched = source_tokens & target_tokens
        missing = target_tokens - source_tokens

        sim = SimilarityCalculator.cosine_similarity(source_text, target_text)

        return {
            "similarity_score": sim,
            "matched_keywords": sorted(list(matched)),
            "missing_keywords": sorted(list(missing)),
            "match_count": len(matched)
        }


class KeywordRanker:
    @staticmethod
    def rank(text: str, top_n: int = 10) -> List[Dict[str, Any]]:
        tokens = Tokenizer.tokenize(text)
        counts = Counter(tokens)
        return [{"keyword": k, "frequency": v} for k, v in counts.most_common(top_n)]


ACTION_VERBS = [
    "achieved", "architected", "built", "created", "designed", "developed",
    "engineered", "implemented", "improved", "increased", "led", "managed",
    "optimized", "reduced", "spearheaded", "streamlined", "transformed"
]


class GrammarChecker:
    @staticmethod
    def check_quality(text: str) -> Dict[str, Any]:
        if not text:
            return {"score": 50, "action_verb_count": 0, "bullets": 0}

        text_lower = text.lower()
        found_verbs = [v for v in ACTION_VERBS if v in text_lower]

        lines = [l for l in text.splitlines() if l.strip()]
        bullet_count = len(lines)

        quality_score = min(60 + (len(found_verbs) * 5), 100)

        return {
            "score": quality_score,
            "action_verbs_found": found_verbs,
            "action_verb_count": len(found_verbs),
            "bullet_count": bullet_count
        }


class Summarizer:
    @staticmethod
    def summarize(text: str, max_sentences: int = 3) -> str:
        if not text:
            return ""
        lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 20]
        return " ".join(lines[:max_sentences])
