"""
=========================================================
AI Career Intelligence Platform
Email Service
=========================================================
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import current_app


class EmailService:
    """
    Email Dispatch Business Logic
    """

    @staticmethod
    def send_email(to_email: str, subject: str, body: str) -> bool:
        """
        Send an email notification via SMTP or simulate send in dev mode.
        """
        mail_server = current_app.config.get("MAIL_SERVER")
        mail_port = current_app.config.get("MAIL_PORT", 587)
        mail_user = current_app.config.get("MAIL_USERNAME")
        mail_pass = current_app.config.get("MAIL_PASSWORD")

        if not mail_server or not mail_user:
            print(f"[DEV EMAIL LOG] To: {to_email} | Subject: {subject} | Body: {body[:100]}...")
            return True

        try:
            msg = MIMEMultipart()
            msg["From"] = mail_user
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "html"))

            server = smtplib.SMTP(mail_server, mail_port)
            if current_app.config.get("MAIL_USE_TLS", True):
                server.starttls()
            server.login(mail_user, mail_pass)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as err:
            print("Email sending failed:", err)
            return False
