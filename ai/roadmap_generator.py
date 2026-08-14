"""
=========================================================
AI Career Intelligence Platform
Skill Roadmap Generator
=========================================================
"""

from typing import Dict, Any, List
from ai.gemini_client import GeminiClient
from ai.prompt_templates import ROADMAP_PROMPT


class RoadmapGenerator:
    """
    Generate 90-day career roadmap tailored to candidate target roles.
    """

    def __init__(self):
        self.client = GeminiClient()

    def generate(self, target_role: str, current_skills: List[str] = None) -> Dict[str, Any]:
        skills_str = ", ".join(current_skills) if current_skills else "Basic Python, SQL"
        prompt = ROADMAP_PROMPT.format(
            target_role=target_role,
            current_skills=skills_str
        )

        res = self.client.generate_json(prompt)
        if isinstance(res, dict) and "phase_1_30_days" in res:
            return res

        # Fallback structured roadmap
        return {
            "target_role": target_role,
            "phase_1_30_days": {
                "title": "Core Skill Foundation & Modern Tools",
                "goals": [
                    f"Master core competencies for {target_role}.",
                    "Build strong project structure with Git & GitHub workflow.",
                    "Implement clean RESTful APIs and unit testing."
                ],
                "key_skills": ["Python", "REST API", "SQL", "Git"],
                "recommended_projects": ["Build an API Service with CRUD endpoints."]
            },
            "phase_2_60_days": {
                "title": "Advanced Engineering & Ecosystem Integration",
                "goals": [
                    "Integrate relational databases and modern ORMs.",
                    "Set up containerization with Docker and deployment pipelines.",
                    "Apply authentication and security best practices."
                ],
                "key_skills": ["PostgreSQL", "Docker", "JWT", "Redis"],
                "recommended_projects": ["Containerized Microservice with Cache & Auth."]
            },
            "phase_3_90_days": {
                "title": "AI Integration, System Design & Interview Readiness",
                "goals": [
                    "Incorporate AI APIs and RAG document retrieval.",
                    "Optimize system throughput and ATS resume scoring.",
                    "Complete mock technical interviews and portfolio polish."
                ],
                "key_skills": ["System Design", "Gemini API", "FAISS", "CI/CD"],
                "recommended_projects": ["End-to-End AI-Powered Web Application."]
            }
        }
