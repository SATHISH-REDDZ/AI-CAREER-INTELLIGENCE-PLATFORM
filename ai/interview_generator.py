"""
=========================================================
AI Career Intelligence Platform
Interview Questions Generator
=========================================================
"""

from typing import List, Dict, Any
from ai.gemini_client import GeminiClient
from ai.prompt_templates import INTERVIEW_QUESTION_PROMPT

DEFAULT_QUESTIONS = {
    "Python Developer": [
        {
            "id": 1,
            "category": "Technical",
            "question": "How do Python memory management and garbage collection work under the hood?",
            "tips": "Mention reference counting, generational garbage collector (gc module), and cyclic references."
        },
        {
            "id": 2,
            "category": "Behavioral",
            "question": "Describe a situation where you had to optimize a slow-performing API or database query.",
            "tips": "Use the STAR method: Situation, Task, Action, Result. Highlight indexing or caching strategies."
        },
        {
            "id": 3,
            "category": "Coding",
            "question": "Write a Python function to detect circular dependency in a directed graph of task dependencies.",
            "tips": "Discuss Topological Sort using Kahn's algorithm or DFS with visited states."
        }
    ],
    "Data Analyst": [
        {
            "id": 1,
            "category": "Technical",
            "question": "What is the difference between INNER JOIN, LEFT JOIN, and FULL OUTER JOIN in SQL?",
            "tips": "Provide clear examples showing matching rows and NULL values."
        },
        {
            "id": 2,
            "category": "Behavioral",
            "question": "Tell me about a time when business stakeholders disagreed with your data findings.",
            "tips": "Focus on data storytelling, visual evidence, and collaborative problem-solving."
        }
    ]
}


class InterviewGenerator:
    """
    Generate mock interview questions for targeted job roles.
    """

    def __init__(self):
        self.client = GeminiClient()

    def generate(self, target_role: str = "Python Developer", difficulty: str = "Medium", count: int = 3) -> List[Dict[str, Any]]:
        prompt = INTERVIEW_QUESTION_PROMPT.format(
            target_role=target_role,
            difficulty=difficulty,
            count=count
        )
        res = self.client.generate_json(prompt)
        if isinstance(res, list) and len(res) > 0:
            return res

        # Fallback to predefined rich question bank
        questions = DEFAULT_QUESTIONS.get(target_role, DEFAULT_QUESTIONS["Python Developer"])
        return questions[:count]
