"""
=========================================================
AI Career Intelligence Platform
NLP Skill Extractor
=========================================================
"""

import re

TECH_SKILLS = [
    "Python", "Flask", "Django", "FastAPI", "Java", "C++", "C#", "SQL",
    "PostgreSQL", "MySQL", "MongoDB", "Redis", "Docker", "Kubernetes",
    "AWS", "Azure", "GCP", "Git", "GitHub", "Linux", "REST API",
    "GraphQL", "Pandas", "NumPy", "Scikit-learn", "TensorFlow",
    "PyTorch", "spaCy", "NLTK", "LangChain", "FAISS", "Tableau",
    "Power BI", "React", "Vue", "Angular", "JavaScript", "TypeScript",
    "HTML", "CSS", "TailwindCSS", "Node.js", "Express", "pytest"
]


class SkillExtractor:
    """
    NLP Skill Extractor using Regex & Tokenization
    """

    @staticmethod
    def extract_skills(text: str) -> list:
        """
        Extract technical skills present in text.
        """
        if not text:
            return []

        text_lower = text.lower()
        extracted = []

        for skill in TECH_SKILLS:
            # Match word boundary for precision
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, text_lower):
                extracted.append(skill)

        return sorted(list(set(extracted)))
