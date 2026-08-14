"""
=========================================================
AI Career Intelligence Platform
ML Predictor Facade
=========================================================
"""

from typing import Dict, Any
from ml.ats_score import ATSScoreCalculator
from ml.skill_gap import SkillGapAnalyzer, JobMatcher
from ml.career_prediction import CareerPredictor
from ml.salary_prediction import SalaryPredictor


class MLPredictor:
    """
    Unified predictor facade for ATS scoring, career role prediction, skill gaps, and salary ranges.
    """

    @staticmethod
    def full_analysis(resume_text: str, target_role: str = "Python Developer") -> Dict[str, Any]:
        ats_res = ATSScoreCalculator.calculate_score(resume_text, target_role)
        predicted_role = CareerPredictor.predict_role(ats_res["extracted_skills"])
        gap_res = SkillGapAnalyzer.analyze(resume_text, target_role)
        salary_range = SalaryPredictor.estimate_salary(target_role, len(ats_res["extracted_skills"]))
        job_matches = JobMatcher.match_jobs(ats_res["extracted_skills"])

        return {
            "ats_result": ats_res,
            "predicted_best_role": predicted_role,
            "skill_gap": gap_res,
            "salary_estimate": salary_range,
            "top_job_matches": job_matches[:3]
        }
