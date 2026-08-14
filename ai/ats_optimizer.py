"""
=========================================================
AI Career Intelligence Platform
ATS Optimizer
=========================================================
"""

from typing import Dict, Any, List


class ATSOptimizer:
    """
    ATS Optimizer for targeted resume analysis against job requirements.
    """

    @staticmethod
    def get_optimization_suggestions(missing_skills: List[str], current_score: int) -> Dict[str, Any]:
        critical_suggestions = []
        for skill in missing_skills[:5]:
            critical_suggestions.append(f"Add evidence or project experience using '{skill}' to your skills or work history.")

        return {
            "current_score": current_score,
            "target_score": 90,
            "formatting_tips": [
                "Use standard 0.5-inch to 1-inch margins.",
                "Stick to standard fonts: Inter, Arial, Calibri, or Helvetica.",
                "Ensure standard section headings: 'Summary', 'Skills', 'Experience', 'Projects', 'Education'."
            ],
            "missing_skills_action_plan": critical_suggestions,
            "keyword_density_advice": "Repeat core technical keywords (e.g. Python, SQL, REST API) 2-3 times across projects and experience."
        }
