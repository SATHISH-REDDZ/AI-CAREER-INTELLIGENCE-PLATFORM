"""
=========================================================
AI Career Intelligence Platform
ML Skill Gap & Job Matcher Subsystem
=========================================================
"""

from typing import Dict, Any, List
from nlp.skill_extractor import SkillExtractor
from ml.ats_score import ROLE_TAXONOMY


class SkillGapAnalyzer:
    @staticmethod
    def analyze(candidate_text: str, target_role: str) -> Dict[str, Any]:
        extracted = SkillExtractor.extract_skills(candidate_text)
        required = ROLE_TAXONOMY.get(target_role, ROLE_TAXONOMY["Python Developer"])

        missing = [s for s in required if s not in extracted]
        match_percentage = round((len(required) - len(missing)) / len(required) * 100, 1)

        learning_roadmap = []
        levels = ["Beginner Fundamentals", "Intermediate Frameworks", "Advanced Architecture", "Cloud & Deployment"]
        for idx, skill in enumerate(missing, start=1):
            level_idx = min(idx - 1, len(levels) - 1)
            learning_roadmap.append({
                "step": idx,
                "level": levels[level_idx],
                "skill": skill,
                "action": f"Master {skill} with hands-on project implementation."
            })

        return {
            "target_role": target_role,
            "match_percentage": match_percentage,
            "acquired_skills": extracted,
            "missing_skills": missing,
            "critical_gap_count": len(missing),
            "learning_roadmap": learning_roadmap
        }


class JobMatcher:
    @staticmethod
    def match_jobs(candidate_skills: List[str], available_jobs: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        if not available_jobs:
            available_jobs = [
                {"id": 1, "title": "Senior Python Engineer", "company": "TechCorp", "required_skills": ["Python", "Flask", "Docker", "SQL"]},
                {"id": 2, "title": "AI Platform Engineer", "company": "DataCloud AI", "required_skills": ["Python", "LangChain", "FAISS", "REST API"]},
                {"id": 3, "title": "Data Analyst", "company": "Analytics Global", "required_skills": ["Python", "SQL", "Pandas", "Tableau"]}
            ]

        cand_set = set(s.lower() for s in candidate_skills)
        matched_results = []

        for job in available_jobs:
            req_set = set(s.lower() for s in job.get("required_skills", []))
            overlap = cand_set & req_set
            match_rate = round(len(overlap) / max(len(req_set), 1) * 100, 1)

            matched_results.append({
                "job_id": job.get("id"),
                "title": job.get("title"),
                "company": job.get("company"),
                "match_percentage": match_rate,
                "missing_skills": [s for s in job.get("required_skills", []) if s.lower() not in cand_set]
            })

        matched_results.sort(key=lambda x: x["match_percentage"], reverse=True)
        return matched_results

    @staticmethod
    def match_job_description(candidate_text: str, job_description_text: str) -> Dict[str, Any]:
        """
        Compare candidate resume text directly against a target job description text.
        """
        cand_skills = SkillExtractor.extract_skills(candidate_text)
        jd_skills = SkillExtractor.extract_skills(job_description_text)

        cand_set = set(s.lower() for s in cand_skills)
        jd_set = set(s.lower() for s in jd_skills)

        matched_skills = [s for s in jd_skills if s.lower() in cand_set]
        missing_skills = [s for s in jd_skills if s.lower() not in cand_set]

        if jd_skills:
            skill_match_pct = round((len(matched_skills) / len(jd_skills)) * 100, 1)
        else:
            skill_match_pct = 70.0

        # Calculate text similarity
        from nlp.similarity import SimilarityCalculator
        text_similarity = SimilarityCalculator.cosine_similarity(candidate_text, job_description_text)

        final_match_score = round((skill_match_pct * 0.70) + (text_similarity * 100.0 * 0.30), 1)

        return {
            "match_score": final_match_score,
            "skill_match_percentage": skill_match_pct,
            "text_similarity_percentage": round(text_similarity * 100, 1),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "job_description_skills": jd_skills,
            "candidate_skills": cand_skills,
            "recommendation": f"Job alignment is rated at {final_match_score}%. Focus on acquiring {', '.join(missing_skills[:3]) if missing_skills else 'advanced features'} to maximize interview callbacks."
        }
