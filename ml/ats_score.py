"""
=========================================================
AI Career Intelligence Platform
ML ATS Score Calculation Engine
=========================================================
"""

from typing import Dict, Any, List
import re
from nlp.skill_extractor import SkillExtractor
from nlp.keyword_match import GrammarChecker, KeywordRanker
from nlp.parser import ResumeParser

ROLE_TAXONOMY = {
    "Python Developer": ["Python", "Flask", "Django", "SQL", "Git", "REST API", "Docker", "pytest"],
    "Data Analyst": ["Python", "SQL", "Pandas", "NumPy", "Tableau", "Power BI", "Excel"],
    "Machine Learning Engineer": ["Python", "Scikit-learn", "TensorFlow", "PyTorch", "Pandas", "NumPy", "NLP"],
    "Backend Developer": ["Python", "Flask", "SQL", "PostgreSQL", "Docker", "REST API", "Git", "Redis"],
    "AI Engineer": ["Python", "LangChain", "FAISS", "Gemini API", "NLP", "Machine Learning", "PyTorch"]
}


class ATSScoreCalculator:
    """
    Calculate ATS Compatibility Score based on:
    - Skills Match (35%)
    - Keywords (20%)
    - Resume Structure (15%)
    - Experience (10%)
    - Action Verbs (10%)
    - Education (5%)
    - Formatting (5%)
    """

    @staticmethod
    def calculate_score(resume_text: str, target_role: str = "Python Developer") -> Dict[str, Any]:
        if not resume_text:
            return {
                "score": 0.0,
                "skills_match": 0.0,
                "keyword_match": 0.0,
                "structure_score": 0.0,
                "experience_score": 0.0,
                "action_verb_score": 0.0,
                "education_score": 0.0,
                "formatting_score": 0.0,
                "matched_skills": [],
                "missing_skills": ROLE_TAXONOMY.get(target_role, ROLE_TAXONOMY["Python Developer"]),
                "explanation": "Empty resume text provided."
            }

        extracted_skills = SkillExtractor.extract_skills(resume_text)
        required_skills = ROLE_TAXONOMY.get(target_role, ROLE_TAXONOMY["Python Developer"])

        matched_skills = [s for s in required_skills if any(s.lower() in ex.lower() for ex in extracted_skills)]
        missing_skills = [s for s in required_skills if s not in matched_skills]

        # 1. Skills Match (35%)
        skills_match = round((len(matched_skills) / max(len(required_skills), 1)) * 100.0, 1)

        # 2. Keywords Match (20%)
        rankings = KeywordRanker.rank(resume_text, top_n=15)
        kw_count = len(rankings)
        keyword_match = min(100.0, kw_count * 8.0)

        # 3. Resume Structure (15%)
        sections = ResumeParser.parse_sections(resume_text)
        detected_count = sum(1 for k, v in sections.items() if v.strip())
        contact_info = ResumeParser.parse_contact_info(resume_text)
        if contact_info.get("email") or contact_info.get("phone"):
            detected_count += 1
        structure_score = min(100.0, (detected_count / 5.0) * 100.0)

        # 4. Experience (10%)
        exp_text = sections.get("experience", "") or resume_text
        has_years = bool(re.search(r"\b(20\d\d|19\d\d|\d+\+?\s*years?)\b", exp_text, re.IGNORECASE))
        has_bullets = bool(re.search(r"^[-•\*]\s+", exp_text, re.MULTILINE)) or len(exp_text.splitlines()) > 5
        experience_score = 100.0 if (has_years and has_bullets) else (70.0 if (has_years or has_bullets) else 40.0)

        # 5. Action Verbs (10%)
        quality_res = GrammarChecker.check_quality(resume_text)
        action_verb_count = quality_res["action_verb_count"]
        action_verb_score = min(100.0, action_verb_count * 20.0)

        # 6. Education (5%)
        edu_text = sections.get("education", "") or resume_text
        has_degree = bool(re.search(r"\b(b\.?s\.?|m\.?s\.?|bachelor|master|degree|phd|diploma|university|college)\b", edu_text, re.IGNORECASE))
        education_score = 100.0 if has_degree else 30.0

        # 7. Formatting (5%)
        word_count = len(resume_text.split())
        if 250 <= word_count <= 900:
            formatting_score = 100.0
        elif 100 <= word_count < 250 or 900 < word_count <= 1500:
            formatting_score = 70.0
        else:
            formatting_score = 40.0

        # Weighted Total Score
        final_ats_score = round(
            (skills_match * 0.35) +
            (keyword_match * 0.20) +
            (structure_score * 0.15) +
            (experience_score * 0.10) +
            (action_verb_score * 0.10) +
            (education_score * 0.05) +
            (formatting_score * 0.05),
            1
        )

        explanation = (
            f"ATS compatibility score of {final_ats_score}/100 calculated for '{target_role}'. "
            f"Skill match is at {skills_match}% with {len(matched_skills)}/{len(required_skills)} core target skills. "
            f"Resume includes {action_verb_count} strong action verbs, {len(rankings)} keyword signals, and a formatting score of {formatting_score}%."
        )

        return {
            "score": final_ats_score,
            "ats_score": final_ats_score,
            "skills_match": skills_match,
            "keyword_match": round(keyword_match, 1),
            "structure_score": round(structure_score, 1),
            "experience_score": round(experience_score, 1),
            "action_verb_score": round(action_verb_score, 1),
            "education_score": round(education_score, 1),
            "formatting_score": round(formatting_score, 1),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "extracted_skills": extracted_skills,
            "word_count": word_count,
            "explanation": explanation
        }
