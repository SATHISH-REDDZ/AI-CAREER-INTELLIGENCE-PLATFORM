"""
=========================================================
AI Career Intelligence Platform
Job Recommendation Service
=========================================================
"""

# Sample job database catalog
MOCK_JOBS = [
    {
        "id": 1,
        "title": "Junior Python Developer",
        "company": "TechInnovate Inc.",
        "location": "Remote / Hybrid",
        "skills_required": ["Python", "Flask", "SQL", "Git"],
        "salary_range": "$60,000 - $80,000",
        "job_type": "Full-Time"
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "company": "Analytics Core",
        "location": "New York, NY",
        "skills_required": ["Python", "SQL", "Pandas", "Tableau"],
        "salary_range": "$70,000 - $90,000",
        "job_type": "Full-Time"
    },
    {
        "id": 3,
        "title": "Machine Learning Engineer",
        "company": "AI Vision Labs",
        "location": "San Francisco, CA",
        "skills_required": ["Python", "Scikit-learn", "TensorFlow", "Pandas"],
        "salary_range": "$110,000 - $140,000",
        "job_type": "Full-Time"
    },
    {
        "id": 4,
        "title": "Backend Software Engineer",
        "company": "CloudScale Solutions",
        "location": "Austin, TX",
        "skills_required": ["Python", "Flask", "PostgreSQL", "Docker", "REST API"],
        "salary_range": "$95,000 - $125,000",
        "job_type": "Full-Time"
    }
]


class JobService:
    """
    Job Recommendation Engine Business Logic
    """

    @staticmethod
    def get_recommendations(user_skills: list) -> list:
        """
        Calculate match percentages and recommend jobs for user skills.
        """
        user_skills_set = set(s.lower() for s in user_skills)
        recommendations = []

        for job in MOCK_JOBS:
            req_skills = job["skills_required"]
            matches = [s for s in req_skills if s.lower() in user_skills_set]
            match_percentage = round((len(matches) / len(req_skills)) * 100, 1)

            job_rec = dict(job)
            job_rec["match_percentage"] = match_percentage
            job_rec["matched_skills"] = matches
            job_rec["missing_skills"] = [s for s in req_skills if s.lower() not in user_skills_set]
            recommendations.append(job_rec)

        # Sort by highest match score
        recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
        return recommendations
