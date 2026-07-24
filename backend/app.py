from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

from config.db import connect_db

from routes.auth import auth
from routes.history import history
from routes.dashboard import dashboard
from routes.resume import resume
from routes.video import video
from routes.audio import audio
from routes.text import text

# Flask Mail
from services.mail import mail

# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()

# -------------------------
# Create Flask App
# -------------------------
app = Flask(__name__)

# -------------------------
# Enable CORS
# -------------------------
CORS(app)

# -------------------------
# Configuration
# -------------------------
app.config["SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# -------------------------
# Mail Configuration
# -------------------------
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

# -------------------------
# Initialize Extensions
# -------------------------
jwt = JWTManager(app)

@jwt.invalid_token_loader
def invalid_token_callback(error):
    print("INVALID TOKEN:", error)
    return jsonify({
        "success": False,
        "message": error
    }), 401


@jwt.unauthorized_loader
def unauthorized_callback(error):
    print("UNAUTHORIZED:", error)
    return jsonify({
        "success": False,
        "message": error
    }), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    print("TOKEN EXPIRED")
    return jsonify({
        "success": False,
        "message": "Token expired"
    }), 401

mail.init_app(app)

# -------------------------
# Connect MongoDB
# -------------------------
connect_db()

# -------------------------
# Register Blueprints
# -------------------------
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(history, url_prefix="/api/history")
app.register_blueprint(dashboard, url_prefix="/api/dashboard")
app.register_blueprint(resume, url_prefix="/api/resume")
app.register_blueprint(video, url_prefix="/api/video")
app.register_blueprint(audio, url_prefix="/api/audio")
app.register_blueprint(text, url_prefix="/api/text")

# -------------------------
# Home Route
# -------------------------
@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "🚀 SummarAI Backend Running Successfully!"
    })


# -------------------------
# Health Check Route
# -------------------------
@app.route("/api/health")
def health():
    import config.db as database

    return jsonify({
        "success": True,
        "database": "connected" if database.db else "disconnected"
    })


# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=True
    )