import config.db as database
from models.history import History
from bson import ObjectId


class HistoryService:

    # ----------------------------
    # Save History
    # ----------------------------
    @staticmethod
    def save_history(
        user_id,
        module,
        file_name,
        summary,
        processing_time=0,
        status="Completed",
    ):
        history_collection = database.db["history"]

        history = History(
            user_id=user_id,
            module=module,
            file_name=file_name,
            summary=summary,
            processing_time=processing_time,
            status=status,
        )

        result = history_collection.insert_one(history.to_dict())

        return str(result.inserted_id)

    # ----------------------------
    # Get User History
    # ----------------------------
    @staticmethod
    def get_user_history(user_id):
        history_collection = database.db["history"]

        history = history_collection.find(
            {"user_id": user_id}
        ).sort("created_at", -1)

        history_list = []

        for item in history:
            history_list.append({
                "id": str(item["_id"]),
                "module": item["module"],
                "file_name": item["file_name"],
                "summary": item["summary"],
                "processing_time": item["processing_time"],
                "status": item["status"],
                "created_at": str(item["created_at"]),
            })

        return history_list

    # ----------------------------
    # Delete One History
    # ----------------------------
    @staticmethod
    def delete_history(user_id, history_id):
        history_collection = database.db["history"]

        result = history_collection.delete_one({
            "_id": ObjectId(history_id),
            "user_id": user_id
        })

        return result.deleted_count > 0

    # ----------------------------
    # Clear All History
    # ----------------------------
    @staticmethod
    def clear_history(user_id):
        history_collection = database.db["history"]

        result = history_collection.delete_many({
            "user_id": user_id
        })

        return result.deleted_count