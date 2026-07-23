from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = None
db = None


def connect_db():
    global client, db

    try:
        mongo_uri = os.getenv("MONGO_URI")

        client = MongoClient(mongo_uri)

        client.admin.command("ping")

        db = client["summarai"]

        print("✅ MongoDB Connected Successfully!")

        return db

    except Exception as e:
        print("❌ MongoDB Connection Failed!")
        print(e)
        return None