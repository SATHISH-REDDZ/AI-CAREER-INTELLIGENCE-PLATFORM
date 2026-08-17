"""
=========================================================
AI Career Intelligence Platform
ML Career Role Prediction Model
=========================================================
"""


class CareerPredictor:
    """
    Predict best-fit job role from candidate skill vector.
    """

    ROLE_SKILL_MATRIX = {
        "Python Developer": {"python", "flask", "django", "sql", "git", "rest api"},
        "Data Analyst": {"python", "sql", "pandas", "numpy", "tableau", "power bi"},
        "Machine Learning Engineer": {"python", "scikit-learn", "tensorflow", "pytorch", "pandas", "nlp"},
        "Backend Developer": {"python", "flask", "postgresql", "docker", "redis"},
        "AI Engineer": {"python", "langchain", "faiss", "gemini api", "nlp"}
    }

    @classmethod
    def predict_role(cls, candidate_skills: list) -> str:
        """
        Predict best matching career role based on skill overlap.
        """
        recommendations = cls.recommend_roles(candidate_skills)
        return recommendations[0]["role"] if recommendations else "Python Developer"

    @classmethod
    def recommend_roles(cls, candidate_skills: list) -> list:
        """
        Generate detailed career recommendations for candidate skills.
        """
        skills_set = set(s.lower() for s in candidate_skills)
        results = []

        for role, required in cls.ROLE_SKILL_MATRIX.items():
            matched = sorted(list(skills_set & required))
            missing = sorted(list(required - skills_set))
            match_percentage = round((len(matched) / max(len(required), 1)) * 100, 1)

            why = (
                f"Matches {len(matched)} key requirement(s) ({', '.join(matched) if matched else 'General background'}). "
                f"Acquiring {', '.join(missing[:3]) if missing else 'advanced concepts'} will boost your profile."
            )

            results.append({
                "role": role,
                "match_percentage": match_percentage,
                "why": why,
                "matched_skills": [s.title() for s in matched],
                "missing_skills": [s.title() for s in missing],
                "recommended_learning": [s.title() for s in missing]
            })

        results.sort(key=lambda x: x["match_percentage"], reverse=True)
        return results


# Backward compatibility alias
CareerPredictionEngine = CareerPredictor

