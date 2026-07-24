from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

from config.db import connect_db

from routes.auth import auth
from routes.history import history
from routes.dashboard import dashboard

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Configuration
app.config["SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# Initialize JWT
jwt = JWTManager(app)

# Connect to MongoDB
connect_db()

# -------------------------
# Register Blueprints
# -------------------------
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(history, url_prefix="/api/history")
app.register_blueprint(dashboard, url_prefix="/api/dashboard")


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