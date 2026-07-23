import config.db as database
from models.history import History


class HistoryService:

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