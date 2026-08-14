"""
=========================================================
AI Career Intelligence Platform
AI Subsystem Helpers
=========================================================
"""

from typing import Dict, Any, List


class CareerCoach:
    @staticmethod
    def get_advice(target_role: str, years_exp: int = 1) -> str:
        return f"For a candidate targeting {target_role} with {years_exp} years experience: Focus on building high-impact portfolio projects, actively networking on LinkedIn, and practicing STAR behavioral interview scenarios."


class CodingMentor:
    @staticmethod
    def review_code(code_snippet: str, language: str = "python") -> Dict[str, Any]:
        return {
            "language": language,
            "quality_score": 85,
            "suggestions": [
                "Ensure type hints are provided for parameters and return types.",
                "Add docstrings describing function arguments and potential exceptions.",
                "Include unit test coverage using pytest."
            ]
        }


class JobDescriptionAnalyzer:
    @staticmethod
    def extract_requirements(jd_text: str) -> Dict[str, Any]:
        return {
            "required_skills": ["Python", "SQL", "REST API", "Docker"],
            "experience_level": "Mid-Level",
            "key_responsibilities": [
                "Design and maintain scalable web services.",
                "Collaborate with product and frontend engineering teams."
            ]
        }


class LearningAdvisor:
    @staticmethod
    def get_resources(missing_skills: List[str]) -> List[Dict[str, str]]:
        resources = []
        for skill in missing_skills:
            resources.append({
                "skill": skill,
                "recommended_course": f"Mastering {skill} - FreeCodeCamp / Coursera",
                "documentation": f"Official {skill} Documentation"
            })
        return resources


class SalaryAdvisor:
    @staticmethod
    def estimate_salary(target_role: str, experience_years: int = 2) -> Dict[str, Any]:
        base = 75000 + (experience_years * 12000)
        return {
            "target_role": target_role,
            "min_salary": base - 10000,
            "median_salary": base,
            "max_salary": base + 20000,
            "currency": "USD"
        }


class GithubAdvisor:
    @staticmethod
    def suggest_projects(target_role: str) -> List[Dict[str, str]]:
        return [
            {
                "title": f"AI-Powered {target_role} Dashboard",
                "description": "Full-stack web platform using Flask, REST APIs, SQLite/PostgreSQL, and Google Gemini API.",
                "tech_stack": "Python, Flask, SQLite, HTML/CSS/JS, Gemini API"
            },
            {
                "title": "Microservices Task Pipeline",
                "description": "Asynchronous job worker processing data with Redis queue and Docker.",
                "tech_stack": "Python, Celery, Redis, Docker"
            }
        ]
