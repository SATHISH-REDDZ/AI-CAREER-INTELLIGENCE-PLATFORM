"""
=========================================================
AI Career Intelligence Platform
Cover Letter Generator
=========================================================
"""

from typing import Dict, Any
from ai.gemini_client import GeminiClient
from ai.prompt_templates import COVER_LETTER_PROMPT


class CoverLetterGenerator:
    """
    Generates tailored cover letters for candidate target roles and companies.
    """

    def __init__(self):
        self.client = GeminiClient()

    def generate(self, resume_text: str, target_role: str, company_name: str = "Target Organization") -> str:
        prompt = COVER_LETTER_PROMPT.format(
            resume_text=resume_text[:2000] if resume_text else "Experienced tech professional with strong background.",
            target_role=target_role,
            company_name=company_name
        )

        letter = self.client.generate_text(prompt)
        if letter:
            return letter

        # Fallback template generator
        return (
            f"Dear Hiring Manager at {company_name},\n\n"
            f"I am writing to express my strong enthusiasm for the {target_role} position. "
            f"With a proven background in software development, problem-solving, and building robust technical applications, "
            f"I am confident in my ability to deliver immediate value to your engineering team.\n\n"
            f"My key experience includes designing scalable backends, working with modern databases, and collaborating on end-to-end projects. "
            f"I excel at translating complex technical requirements into high-quality code.\n\n"
            f"Thank you for considering my application. I look forward to discussing how my skills align with {company_name}'s goals.\n\n"
            f"Sincerely,\nCandidate"
        )
