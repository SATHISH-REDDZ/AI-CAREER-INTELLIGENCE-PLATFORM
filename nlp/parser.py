"""
=========================================================
AI Career Intelligence Platform
Resume Section & Contact Parser
=========================================================
"""

import re
from typing import Dict, Any


class ResumeParser:
    """
    Parse Resume Text into Education, Experience, Skills, and Contact Info.
    """

    @staticmethod
    def parse_contact_info(text: str) -> Dict[str, str]:
        contact = {
            "email": "",
            "phone": "",
            "linkedin": "",
            "github": ""
        }
        if not text:
            return contact

        # Email regex
        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
        if email_match:
            contact["email"] = email_match.group(0)

        # Phone regex
        phone_match = re.search(r"\(?\+?\d{1,3}\)?[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}", text)
        if phone_match:
            contact["phone"] = phone_match.group(0)

        # LinkedIn link
        linkedin_match = re.search(r"linkedin\.com/in/[\w-]+", text, re.IGNORECASE)
        if linkedin_match:
            contact["linkedin"] = f"https://www.{linkedin_match.group(0)}"

        # GitHub link
        github_match = re.search(r"github\.com/[\w-]+", text, re.IGNORECASE)
        if github_match:
            contact["github"] = f"https://www.{github_match.group(0)}"

        return contact

    @staticmethod
    def parse_sections(text: str) -> Dict[str, str]:
        """
        Segment raw resume text into key sections.
        """
        sections = {
            "education": "",
            "experience": "",
            "skills": "",
            "projects": ""
        }

        if not text:
            return sections

        lines = text.splitlines()
        current_section = None

        for line in lines:
            line_clean = line.strip().lower()
            if re.search(r"\b(education|academic|qualification)\b", line_clean):
                current_section = "education"
                continue
            elif re.search(r"\b(experience|employment|work history|career)\b", line_clean):
                current_section = "experience"
                continue
            elif re.search(r"\b(skills|technical skills|competencies)\b", line_clean):
                current_section = "skills"
                continue
            elif re.search(r"\b(projects|key projects|portfolio)\b", line_clean):
                current_section = "projects"
                continue

            if current_section:
                sections[current_section] += line + "\n"

        return sections
