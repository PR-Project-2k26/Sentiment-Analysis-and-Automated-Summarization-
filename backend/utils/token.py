from itsdangerous import URLSafeTimedSerializer
from flask import current_app


def get_serializer():
    """
    Create a serializer using the app's secret key.
    """
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])


def generate_reset_token(email):
    """
    Generate a secure password reset token.
    """
    serializer = get_serializer()
    return serializer.dumps(email, salt="password-reset-salt")


def verify_reset_token(token, expires_sec=1800):
    """
    Verify the reset token.

    expires_sec = 1800 seconds = 30 minutes
    """
    serializer = get_serializer()

    try:
        email = serializer.loads(
            token,
            salt="password-reset-salt",
            max_age=expires_sec
        )
        return email

    except Exception:
        return None