"""
=========================================================
AI Career Intelligence Platform
Career Roadmap Service
=========================================================
"""

from ai.roadmap_generator import RoadmapGenerator

ROADMAP_TEMPLATES = {
    "Python Developer": [
        {"milestone": 1, "topic": "Advanced Python & OOP", "duration": "2 Weeks", "status": "In Progress"},
        {"milestone": 2, "topic": "Flask & SQLAlchemy REST API Development", "duration": "3 Weeks", "status": "Pending"},
        {"milestone": 3, "topic": "Docker Containerization & CI/CD Pipelines", "duration": "2 Weeks", "status": "Pending"},
        {"milestone": 4, "topic": "Cloud Deployment (AWS / Render)", "duration": "2 Weeks", "status": "Pending"}
    ],
    "Data Analyst": [
        {"milestone": 1, "topic": "Advanced SQL & Query Optimization", "duration": "2 Weeks", "status": "In Progress"},
        {"milestone": 2, "topic": "Data Cleaning with Pandas & NumPy", "duration": "2 Weeks", "status": "Pending"},
        {"milestone": 3, "topic": "Data Visualization with Tableau & Power BI", "duration": "3 Weeks", "status": "Pending"}
    ]
}


class RoadmapService:
    """
    Personalized Career Roadmap Generator Logic
    """

    @staticmethod
    def generate_roadmap(user_id: int, target_role: str = "Python Developer") -> dict:
        generator = RoadmapGenerator()
        ai_roadmap = generator.generate(target_role)
        return {
            "success": True,
            "target_role": target_role,
            "roadmap": ai_roadmap
        }

    @staticmethod
    def get_roadmap_for_role(target_role: str = "Python Developer") -> dict:
        roadmap = ROADMAP_TEMPLATES.get(target_role, ROADMAP_TEMPLATES["Python Developer"])
        return {
            "success": True,
            "target_role": target_role,
            "roadmap": roadmap
        }
