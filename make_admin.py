"""
=========================================================
AI Career Intelligence Platform
Make Admin Script
=========================================================
"""

from app import create_app
from app.extensions import db
from models.user import User

app = create_app()

with app.app_context():

    user = User.query.filter_by(
        email="sathish@example.com"
    ).first()

    if user:
        user.role = "admin"

        db.session.commit()

        print("=" * 50)
        print("User role updated successfully!")
        print(f"Email : {user.email}")
        print(f"Role  : {user.role}")
        print("=" * 50)

    else:
        print("User not found.")