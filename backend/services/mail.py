from flask_mail import Mail, Message
from flask import current_app

mail = Mail()


def send_reset_email(email, reset_link):
    """
    Send password reset email.
    """

    msg = Message(
        subject="Reset your SummarAI password",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[email],
    )

    msg.body = f"""
Hello,

We received a request to reset your password.

Click the link below:

{reset_link}

If you did not request this, simply ignore this email.

Regards,
SummarAI Team
"""

    mail.send(msg)