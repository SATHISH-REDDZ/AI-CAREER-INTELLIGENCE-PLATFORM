"""
=========================================================
AI Career Intelligence Platform
Cover Letter Generator Service
=========================================================
"""

from flask import current_app
from repositories.resume_repository import ResumeRepository


class CoverLetterService:
    """
    AI Cover Letter Generator Logic
    """

    @staticmethod
    def generate_cover_letter(
        user_id: int,
        company_name: str,
        job_title: str,
        job_description: str = "",
        tone: str = "Professional"
    ) -> dict:
        """
        Generate tailored executive cover letter with customizable tone (Professional, Concise, Technical).
        """
        resumes = ResumeRepository.get_by_user(user_id)
        resume = resumes[0] if resumes else None

        candidate_name = "Candidate"
        skills = "Python, Flask, SQL, Machine Learning"
        if resume:
            skills = resume.extracted_text[:200] if resume.extracted_text else skills

        if tone.lower() == "concise":
            cover_letter = (
                f"Dear Hiring Manager at {company_name},\n\n"
                f"I am applying for the {job_title} role. With experience in {skills[:80]}, "
                f"I specialize in building scalable software systems and delivering reliable backend solutions.\n\n"
                f"I would welcome the chance to discuss how my technical skills align with {company_name}'s current initiatives.\n\n"
                f"Best regards,\n{candidate_name}"
            )
        elif tone.lower() == "technical":
            cover_letter = (
                f"Dear Engineering Team at {company_name},\n\n"
                f"I am writing to express my interest in the {job_title} position. "
                f"My core stack includes {skills[:120]}, focusing on clean architecture, API design, database performance, and robust testing.\n\n"
                f"I look forward to contributing to {company_name}'s technical infrastructure and scaling challenges.\n\n"
                f"Sincerely,\n{candidate_name}"
            )
        else:
            cover_letter = (
                f"Dear Hiring Team at {company_name},\n\n"
                f"I am writing to express my strong enthusiasm for the {job_title} position. "
                f"With hands-on expertise in {skills[:100]} and a proven track record of developing scalable applications, "
                f"I am confident in my ability to make an immediate, positive impact on your engineering team.\n\n"
                f"Throughout my career, I have consistently focused on building high-performance backend systems, "
                f"optimizing database queries, and leveraging artificial intelligence to solve complex business challenges. "
                f"Your team's work at {company_name} aligns perfectly with my professional goals and technical passions.\n\n"
                f"Thank you for your time and consideration. I welcome the opportunity to discuss how my technical skills "
                f"and experience align with your team's needs.\n\n"
                f"Sincerely,\n{candidate_name}"
            )

        api_key = current_app.config.get("GEMINI_API_KEY")
        if api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = (
                    f"Write a {tone.lower()} 3-paragraph cover letter for a candidate applying for the role of '{job_title}' "
                    f"at company '{company_name}'. Tone style: {tone}. Candidate skills: {skills}. Job description: {job_description[:500]}."
                )
                res = model.generate_content(prompt)
                if res and res.text:
                    cover_letter = res.text.strip()
            except Exception as err:
                print("Gemini Cover Letter warning:", err)

        return {
            "success": True,
            "company_name": company_name,
            "job_title": job_title,
            "tone": tone,
            "cover_letter": cover_letter
        }
