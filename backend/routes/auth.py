from flask import Blueprint, request, jsonify
from email_validator import validate_email, EmailNotValidError
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
import config.db as database
from models.user import User
from utils.password import hash_password, verify_password

auth = Blueprint("auth", __name__)


# ----------------------------
# Register
# ----------------------------
@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required."
        }), 400

    # Validate Email
    try:
        validate_email(email)
    except EmailNotValidError as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400

    users = database.db["users"]

    # Check if user already exists
    if users.find_one({"email": email.lower()}):
        return jsonify({
            "success": False,
            "message": "Email already registered."
        }), 409

    # Create new user
    new_user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    users.insert_one(new_user.to_dict())

    return jsonify({
        "success": True,
        "message": "Registration successful."
    }), 201


# ----------------------------
# Login
# ----------------------------
@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required."
        }), 400

    users = database.db["users"]

    user = users.find_one({
        "email": email.lower()
    })

    if not user:
        return jsonify({
            "success": False,
            "message": "Invalid email or password."
        }), 401

    if not verify_password(password, user["password"]):
        return jsonify({
            "success": False,
            "message": "Invalid email or password."
        }), 401

    access_token = create_access_token(identity=str(user["_id"]))

    return jsonify({
        "success": True,
        "message": "Login successful.",
        "token": access_token,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
    }), 200

# ----------------------------
# Profile
# ----------------------------
@auth.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    users = database.db["users"]

    user = users.find_one({
        "_id": ObjectId(user_id)
    })

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    return jsonify({
        "success": True,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "created_at": str(user["created_at"])
        }
    }), 200

# ----------------------------
# Update Profile
# ----------------------------
@auth.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():

    data = request.get_json()

    name = data.get("name")

    if not name:
        return jsonify({
            "success": False,
            "message": "Name is required."
        }), 400

    user_id = get_jwt_identity()

    users = database.db["users"]

    result = users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "name": name
            }
        }
    )

    if result.modified_count == 0:
        return jsonify({
            "success": False,
            "message": "No changes made."
        }), 400

    return jsonify({
        "success": True,
        "message": "Profile updated successfully."
    }), 200

# ----------------------------
# Change Password
# ----------------------------
@auth.route("/change-password", methods=["PUT"])
@jwt_required()
def change_password():

    data = request.get_json()

    current_password = data.get("currentPassword")
    new_password = data.get("newPassword")

    if not current_password or not new_password:
        return jsonify({
            "success": False,
            "message": "Current and new passwords are required."
        }), 400

    user_id = get_jwt_identity()

    users = database.db["users"]

    user = users.find_one({
        "_id": ObjectId(user_id)
    })

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    if not verify_password(current_password, user["password"]):
        return jsonify({
            "success": False,
            "message": "Current password is incorrect."
        }), 401

    users.update_one(
        {
            "_id": ObjectId(user_id)
        },
        {
            "$set": {
                "password": hash_password(new_password)
            }
        }
    )

    return jsonify({
        "success": True,
        "message": "Password updated successfully."
    }), 200