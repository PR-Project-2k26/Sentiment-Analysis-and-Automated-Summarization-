from config.db import connect_db
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
db = connect_db()

# Enable CORS
CORS(app)

# Secret Key
app.config["SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")


# -------------------------
# Health Check Route
# -------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "🚀 SummarAI Flask Backend Running Successfully!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend is healthy"
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