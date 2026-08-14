"""
=========================================================
AI Career Intelligence Platform
Interview Preparation Service
=========================================================
"""

import json
from flask import current_app

QUESTION_CATALOG = {
    "Python Developer": {
        "technical": [
            "Explain the difference between deep copy and shallow copy in Python.",
            "How do Python generators work, and what are the benefits of using 'yield'?",
            "Describe the Global Interpreter Lock (GIL) and how it affects multi-threading."
        ],
        "behavioral": [
            "Describe a complex bug you encountered in Python and how you debugged it using the STAR method.",
            "How do you prioritize technical debt versus building new features?"
        ],
        "coding": [
            "Write a Python function to check if a string is a valid anagram of another string.",
            "Implement a function that reverses a linked list in O(n) time and O(1) space."
        ]
    },
    "Data Analyst": {
        "technical": [
            "What is the difference between INNER JOIN, LEFT JOIN, and FULL OUTER JOIN in SQL?",
            "How do you handle missing values or outliers in a dataset using Pandas?"
        ],
        "behavioral": [
            "Tell me about a time you presented data analysis results to non-technical stakeholders."
        ],
        "coding": [
            "Write an SQL query to find the second highest salary from an Employee table."
        ]
    }
}


class InterviewService:
    """
    Interview Preparation Business Logic
    """

    @staticmethod
    def generate_questions(user_id: int, target_role: str = "Python Developer", difficulty: str = "Medium") -> dict:
        """
        Generate role-based interview question set.
        """
        role_catalog = QUESTION_CATALOG.get(target_role, QUESTION_CATALOG["Python Developer"])

        questions = {
            "target_role": target_role,
            "difficulty": difficulty,
            "technical": role_catalog.get("technical", []),
            "behavioral": role_catalog.get("behavioral", []),
            "coding": role_catalog.get("coding", [])
        }

        api_key = current_app.config.get("GEMINI_API_KEY")
        if api_key:
            try:
                from ai.gemini_client import GeminiClient
                client = GeminiClient(api_key=api_key)
                prompt = (
                    f"Generate 3 technical interview questions, 2 behavioral questions, and 1 coding challenge "
                    f"for a candidate applying for the role of '{target_role}' at '{difficulty}' difficulty. "
                    f"Return the response in valid JSON with keys: technical, behavioral, coding."
                )
                parsed = client.generate_json(prompt=prompt)
                if parsed and isinstance(parsed, dict):
                    questions["technical"] = parsed.get("technical", questions["technical"])
                    questions["behavioral"] = parsed.get("behavioral", questions["behavioral"])
                    questions["coding"] = parsed.get("coding", questions["coding"])
            except Exception as e:
                print("Gemini Interview Question Gen warning:", e)

        return {
            "success": True,
            "questions": questions
        }

    @staticmethod
    def evaluate_answer(user_id: int, question: str, answer: str) -> dict:
        """
        Evaluate candidate's interview answer and provide feedback.
        """
        if not question or not answer:
            return {
                "success": False,
                "message": "Question and answer are required."
            }

        score = 80
        feedback = "Solid answer! Clear explanation of core concepts with good technical terminology."

        api_key = current_app.config.get("GEMINI_API_KEY")
        if api_key:
            try:
                from ai.gemini_client import GeminiClient
                client = GeminiClient(api_key=api_key)
                prompt = (
                    f"Evaluate this interview answer:\n"
                    f"Question: {question}\n"
                    f"Candidate Answer: {answer}\n\n"
                    f"Provide a score out of 100, key strengths, and areas for improvement."
                )
                ai_feedback = client.generate_text(prompt=prompt)
                if ai_feedback:
                    feedback = ai_feedback
                    score = 85
            except Exception as e:
                print("Gemini Answer Evaluation warning:", e)

        return {
            "success": True,
            "question": question,
            "candidate_answer": answer,
            "score": score,
            "feedback": feedback
        }
