from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = None
db = None

def connect_db():
    global client, db

    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        db = client["summarai"]

        client.admin.command("ping")

        print("✅ MongoDB Connected Successfully!")

        return db

    except Exception as e:
        print(f"❌ MongoDB Connection Error: {e}")
        return None