from datetime import datetime


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email.lower()
        self.password = password
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
        }