"""
=========================================================
AI Career Intelligence Platform
Database Seed Script
=========================================================
"""

from app.extensions import db
from models.user import User
from models.skill import Skill
from models.job import Job


def seed_database():
    """
    Insert initial system data into the database (Users, Skills, Jobs).
    """
    # 1. Seed Default Accounts if missing
    if User.query.count() == 0:
        admin = User(
            full_name="Administrator",
            email="admin@careerai.com",
            role="admin",
            is_verified=True
        )
        admin.set_password("admin123")

        demo_user = User(
            full_name="Alex Johnson",
            email="alex.johnson@example.com",
            role="user",
            is_verified=True
        )
        demo_user.set_password("user123")

        db.session.add_all([admin, demo_user])
        db.session.commit()
        print("[SEED] Default Users Created: admin@careerai.com / alex.johnson@example.com")

    # 2. Seed Skills if missing
    if Skill.query.count() == 0:
        skills_data = [
            # Technical Skills
            ("Python", "Programming Languages", "High", "https://docs.python.org/3/"),
            ("SQL", "Databases", "High", "https://www.w3schools.com/sql/"),
            ("Flask", "Web Frameworks", "High", "https://flask.palletsprojects.com/"),
            ("Django", "Web Frameworks", "High", "https://docs.djangoproject.com/"),
            ("FastAPI", "Web Frameworks", "High", "https://fastapi.tiangolo.com/"),
            ("PostgreSQL", "Databases", "High", "https://www.postgresql.org/docs/"),
            ("MongoDB", "Databases", "Medium", "https://docs.mongodb.com/"),
            ("Redis", "Caching & Messaging", "Medium", "https://redis.io/documentation"),
            ("Docker", "DevOps & Containers", "High", "https://docs.docker.com/"),
            ("Kubernetes", "DevOps & Cloud", "High", "https://kubernetes.io/docs/"),
            ("Git", "Version Control", "High", "https://git-scm.com/doc"),
            ("REST API", "Backend Architecture", "High", "https://restfulapi.net/"),
            ("GraphQL", "API Architectures", "Medium", "https://graphql.org/learn/"),
            ("Pandas", "Data Science", "High", "https://pandas.pydata.org/docs/"),
            ("NumPy", "Data Science", "High", "https://numpy.org/doc/"),
            ("Scikit-learn", "Machine Learning", "High", "https://scikit-learn.org/stable/"),
            ("TensorFlow", "Deep Learning", "High", "https://www.tensorflow.org/learn"),
            ("PyTorch", "Deep Learning", "High", "https://pytorch.org/tutorials/"),
            ("spaCy", "NLP", "Medium", "https://spacy.io/usage"),
            ("FAISS", "Vector Search & RAG", "High", "https://faiss.ai/"),
            ("LangChain", "Generative AI", "High", "https://python.langchain.com/"),
            ("React", "Frontend", "High", "https://react.dev/"),
            ("TypeScript", "Frontend", "High", "https://www.typescriptlang.org/docs/"),
            ("AWS", "Cloud Computing", "High", "https://aws.amazon.com/getting-started/"),
            ("CI/CD", "DevOps", "High", "https://about.gitlab.com/topics/ci-cd/"),
            ("pytest", "Testing", "High", "https://docs.pytest.org/"),

            # Soft & Professional Skills
            ("Problem Solving", "Professional", "High", "https://counseling.online.wfu.edu/blog/problem-solving-skills/"),
            ("System Design", "Architecture", "High", "https://github.com/donnemartin/system-design-primer"),
            ("Agile / Scrum", "Methodologies", "Medium", "https://www.scrum.org/resources/what-is-scrum"),
            ("Communication", "Soft Skills", "High", "https://hbr.org/topic/communication")
        ]

        for name, category, demand, res in skills_data:
            skill_obj = Skill(
                name=name,
                category=category,
                demand_level=demand,
                learning_resource=res,
                description=f"Core skill for modern backend, cloud, data, and AI applications."
            )
            db.session.add(skill_obj)
        db.session.commit()
        print(f"[SEED] Seeded {len(skills_data)} Skills into database.")

    # 3. Seed Jobs if missing
    if Job.query.count() == 0:
        jobs_data = [
            {
                "title": "Python Backend Developer",
                "company": "TechScale Solutions",
                "location": "Remote / Hybrid",
                "employment_type": "Full-Time",
                "experience_level": "Mid-Level",
                "salary": "$95,000 - $125,000",
                "description": "Building microservices, REST APIs, and database pipelines using Python, Flask, PostgreSQL, and Docker.",
                "required_skills": "Python, Flask, PostgreSQL, Docker, REST API, Git, pytest",
                "application_url": "https://careers.techscale.example.com/job/python-backend"
            },
            {
                "title": "Machine Learning Engineer",
                "company": "Cognitive AI Labs",
                "location": "San Francisco, CA",
                "employment_type": "Full-Time",
                "experience_level": "Senior",
                "salary": "$135,000 - $175,000",
                "description": "Designing ML models, vector search indexing, spaCy NLP pipelines, and LangChain RAG integrations.",
                "required_skills": "Python, Scikit-learn, PyTorch, spaCy, FAISS, LangChain, Pandas, NumPy, Docker",
                "application_url": "https://careers.cognitiveai.example.com/job/ml-engineer"
            },
            {
                "title": "Data Analyst",
                "company": "Apex Global Analytics",
                "location": "New York, NY",
                "employment_type": "Full-Time",
                "experience_level": "Junior / Entry",
                "salary": "$70,000 - $90,000",
                "description": "Extracting data insights, building SQL queries, statistical reporting, and pandas data frames.",
                "required_skills": "Python, SQL, Pandas, NumPy, Communication, Problem Solving",
                "application_url": "https://careers.apexanalytics.example.com/job/data-analyst"
            },
            {
                "title": "Full Stack Engineer (Python/React)",
                "company": "NextGen Software",
                "location": "Austin, TX",
                "employment_type": "Full-Time",
                "experience_level": "Mid-Level",
                "salary": "$110,000 - $140,000",
                "description": "Developing robust RESTful APIs with Flask/FastAPI and modern interactive web UIs with React/TypeScript.",
                "required_skills": "Python, Flask, React, TypeScript, REST API, SQL, Git, Docker",
                "application_url": "https://careers.nextgen.example.com/job/fullstack-engineer"
            },
            {
                "title": "DevOps & Cloud Systems Engineer",
                "company": "CloudArmor Infrastructure",
                "location": "Seattle, WA",
                "employment_type": "Full-Time",
                "experience_level": "Mid-Senior",
                "salary": "$125,000 - $160,000",
                "description": "Automating cloud infrastructure, CI/CD pipelines, Docker containerization, and AWS Kubernetes clusters.",
                "required_skills": "Docker, Kubernetes, AWS, CI/CD, Python, Git, System Design",
                "application_url": "https://careers.cloudarmor.example.com/job/devops-engineer"
            }
        ]

        for j in jobs_data:
            job_obj = Job(
                title=j["title"],
                company=j["company"],
                location=j["location"],
                employment_type=j["employment_type"],
                experience_level=j["experience_level"],
                salary=j["salary"],
                description=j["description"],
                required_skills=j["required_skills"],
                application_url=j["application_url"],
                is_active=True
            )
            db.session.add(job_obj)
        db.session.commit()
        print(f"[SEED] Seeded {len(jobs_data)} Job Opportunities into database.")

    print("[SEED] Database seeding complete!")