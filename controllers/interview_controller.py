"""
=========================================================
AI Career Intelligence Platform
Interview Preparation Controller
=========================================================
"""

from flask import jsonify, request, g
from services.interview_service import InterviewService


class InterviewController:
    """
    Interview Preparation Controller
    """

    @staticmethod
    def generate_questions():
        data = request.get_json(silent=True) or {}
        target_role = data.get("target_role", "Python Developer")
        difficulty = data.get("difficulty", "Medium")

        result = InterviewService.generate_questions(
            user_id=g.user_id,
            target_role=target_role,
            difficulty=difficulty
        )
        return jsonify(result), 200

    @staticmethod
    def evaluate_answer():
        data = request.get_json(silent=True) or {}
        question = data.get("question")
        answer = data.get("answer")

        result = InterviewService.evaluate_answer(
            user_id=g.user_id,
            question=question,
            answer=answer
        )
        status_code = 200 if result["success"] else 400
        return jsonify(result), status_code
