"""
=========================================================
AI Career Intelligence Platform
Career Report Generation Service
=========================================================
"""

import json
from models.resume import Resume
from repositories.resume_repository import ResumeRepository


class ReportService:
    """
    Career & Resume Report Generation Logic
    """

    @staticmethod
    def generate_career_report(user_id: int, resume_id: int = None) -> dict:
        """
        Generate comprehensive PDF/JSON career intelligence report.
        """
        if resume_id:
            resume = ResumeRepository.get_by_id(resume_id)
        else:
            resumes = ResumeRepository.get_by_user(user_id)
            resume = resumes[0] if resumes else None

        if not resume:
            return {
                "success": False,
                "message": "No resume found to generate report."
            }

        missing_skills = []
        if resume.missing_skills:
            try:
                missing_skills = json.loads(resume.missing_skills)
            except Exception:
                missing_skills = [resume.missing_skills]

        report_data = {
            "title": "Comprehensive Career Intelligence & ATS Audit Report",
            "candidate_id": user_id,
            "resume_file": resume.file_name,
            "ats_compatibility_score": f"{resume.ats_score}/100",
            "recommended_role": resume.recommended_role or "Python Developer",
            "ai_executive_summary": resume.ai_summary or "Candidate shows strong technical potential.",
            "missing_skills_analysis": missing_skills,
            "action_items": [
                "Optimize ATS resume section headers (Skills, Work Experience, Education).",
                f"Acquire high-priority missing technical skill(s): {', '.join(missing_skills[:3]) if missing_skills else 'Advanced Architecture'}.",
                "Prepare for mock technical interview questions tailored for " + (resume.recommended_role or "Python Developer") + "."
            ]
        }

        return {
            "success": True,
            "report": report_data
        }
