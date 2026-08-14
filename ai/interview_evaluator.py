"""
=========================================================
AI Career Intelligence Platform
Interview Answer Evaluator
=========================================================
"""

from typing import Dict, Any
from ai.gemini_client import GeminiClient
from ai.prompt_templates import INTERVIEW_EVALUATION_PROMPT


class InterviewEvaluator:
    """
    Evaluate candidate interview answers using AI scoring.
    """

    def __init__(self):
        self.client = GeminiClient()

    def evaluate(self, target_role: str, question: str, answer: str) -> Dict[str, Any]:
        if not answer or len(answer.strip()) < 10:
            return {
                "score": 30,
                "strengths": ["Attempted response."],
                "areas_for_improvement": ["Provide more detail.", "Use technical terminology.", "Follow the STAR framework."],
                "missing_keywords": ["specific examples", "impact metrics"],
                "model_answer": "A ideal answer should state the situation, action taken, key technical tools, and measurable result.",
                "feedback_summary": "Your response is too concise. Expand with concrete technical details and outcomes."
            }

        prompt = INTERVIEW_EVALUATION_PROMPT.format(
            target_role=target_role,
            question=question,
            answer=answer
        )

        res = self.client.generate_json(prompt)
        if isinstance(res, dict) and "score" in res:
            return res

        # Rule-based fallback evaluation
        ans_lower = answer.lower()
        score = 65
        strengths = []
        improvements = []

        if len(answer) > 100:
            score += 15
            strengths.append("Good detail length and structural breakdown.")
        else:
            improvements.append("Elaborate further on architectural choices and trade-offs.")

        if any(term in ans_lower for term in ["python", "sql", "api", "database", "optimize", "performance", "test"]):
            score += 10
            strengths.append("Incorporated relevant technical terminology.")
        else:
            improvements.append("Include specific tools, frameworks, and metrics.")

        return {
            "score": min(score, 95),
            "strengths": strengths or ["Clear communication."],
            "areas_for_improvement": improvements or ["Add quantifiable outcome numbers."],
            "missing_keywords": ["architecture", "metrics", "STAR framework"],
            "model_answer": f"For {question}, structure your response clearly: outline the context, technical challenges, your solution, and metrics.",
            "feedback_summary": "Solid foundation! Enhance your answer with specific quantitative results and technical trade-offs."
        }
