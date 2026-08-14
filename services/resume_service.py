"""
=========================================================
AI Career Intelligence Platform
Resume Service
=========================================================
"""

import json
import os
from flask import current_app

from models.resume import Resume
from repositories.resume_repository import ResumeRepository
from services.pdf_service import PDFService
from utils.file_helper import (
    allowed_file,
    save_uploaded_file
)

# Common skills dictionary for skill matching
SKILL_TAXONOMY = {
    "Python Developer": ["Python", "Flask", "Django", "SQL", "Git", "REST API", "Docker", "pytest"],
    "Data Analyst": ["Python", "SQL", "Pandas", "NumPy", "Tableau", "Power BI", "Statistics", "Excel"],
    "Machine Learning Engineer": ["Python", "Scikit-learn", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Machine Learning", "NLP"],
    "Backend Developer": ["Python", "Flask", "SQL", "PostgreSQL", "Docker", "REST API", "Git", "Redis"],
    "AI Engineer": ["Python", "LangChain", "FAISS", "Gemini API", "NLP", "Machine Learning", "PyTorch", "LLM"]
}


class ResumeService:
    """
    Resume Business Logic
    """

    @staticmethod
    def upload_resume(user_id: int, file):
        """
        Upload a resume and extract text.
        """
        print("\n========== SERVICE START ==========")

        if file is None:
            return False, "No file uploaded."

        if file.filename == "":
            return False, "No file selected."

        if not allowed_file(file.filename):
            return False, "Only PDF and DOCX files are allowed."

        filename, filepath, filesize = save_uploaded_file(file)

        extension = os.path.splitext(filename)[1].replace(".", "").lower()

        # Extract text from document
        extracted_text = PDFService.extract_text(filepath)

        resume = Resume(
            user_id=user_id,
            file_name=filename,
            file_path=filepath,
            file_type=extension,
            file_size=filesize,
            extracted_text=extracted_text,
            status="Parsed" if extracted_text else "Uploaded"
        )

        try:
            ResumeRepository.create(resume)
            
            # Automatically perform initial analysis if text was extracted
            if extracted_text:
                ResumeService.analyze_resume(resume.id)

            return True, resume
        except Exception as err:
            print("Repository error:", err)
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                except OSError:
                    pass
            return False, f"Failed to save resume record: {str(err)}"

    @staticmethod
    def analyze_resume(resume_id: int, target_role: str = "Python Developer"):
        """
        Analyze extracted resume text: ATS score, skill extraction, missing skills, AI summary.
        """
        resume = ResumeRepository.get_by_id(resume_id)
        if not resume:
            return False, "Resume not found."

        text = (resume.extracted_text or "").lower()
        if not text:
            # Re-attempt extraction if missing
            extracted_text = PDFService.extract_text(resume.file_path)
            if extracted_text:
                resume.extracted_text = extracted_text
                text = extracted_text.lower()

        # Target role skill matching
        required_skills = SKILL_TAXONOMY.get(target_role, SKILL_TAXONOMY["Python Developer"])
        
        found_skills = []
        missing_skills = []

        # All skills in taxonomy
        all_skills = set(skill for skills in SKILL_TAXONOMY.values() for skill in skills)

        for skill in all_skills:
            if skill.lower() in text:
                found_skills.append(skill)

        # Check missing for target role
        for req in required_skills:
            if req.lower() not in text:
                missing_skills.append(req)

        # Calculate scores
        matched_target_skills = len(required_skills) - len(missing_skills)
        skill_match_percentage = round((matched_target_skills / max(len(required_skills), 1)) * 100, 1)
        ats_score = round(min(100.0, max(30.0, skill_match_percentage + (len(found_skills) * 3))), 1)

        # Simple AI Summary generation
        summary = (
            f"Candidate displays proficiency in key area(s): {', '.join(found_skills[:5]) if found_skills else 'General Skills'}. "
            f"ATS compatibility for target role '{target_role}' is rated at {ats_score}/100. "
            f"Recommended to acquire missing skills: {', '.join(missing_skills) if missing_skills else 'None'}."
        )

        # Call Gemini API for enhanced summary if API key is configured
        gemini_api_key = current_app.config.get("GEMINI_API_KEY")
        if gemini_api_key and text:
            try:
                from ai.gemini_client import GeminiClient
                client = GeminiClient(api_key=gemini_api_key)
                prompt = (
                    f"Analyze this candidate resume for the role of '{target_role}':\n\n{text[:3000]}\n\n"
                    f"Provide a 2-3 sentence executive summary of candidate strengths and key improvement recommendations."
                )
                ai_summary = client.generate_text(prompt=prompt)
                if ai_summary:
                    summary = ai_summary
            except Exception as e:
                print("Gemini API warning:", e)

        # Best matching role prediction
        best_role = target_role
        best_match_count = 0
        for role_name, role_skills in SKILL_TAXONOMY.items():
            matches = sum(1 for s in role_skills if s.lower() in text)
            if matches > best_match_count:
                best_match_count = matches
                best_role = role_name

        ResumeRepository.update_ai_analysis(
            resume=resume,
            resume_score=ats_score,
            ats_score=ats_score,
            skill_match=skill_match_percentage,
            missing_skills=json.dumps(missing_skills),
            ai_summary=summary,
            recommended_role=best_role
        )

        resume.status = "Analyzed"
        ResumeRepository.update(resume)

        return True, resume