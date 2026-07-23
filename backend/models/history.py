from datetime import datetime


class History:
    def __init__(
        self,
        user_id,
        module,
        file_name,
        summary,
        processing_time=0,
        status="Completed",
    ):
        self.user_id = user_id
        self.module = module
        self.file_name = file_name
        self.summary = summary
        self.processing_time = processing_time
        self.status = status
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "module": self.module,
            "file_name": self.file_name,
            "summary": self.summary,
            "processing_time": self.processing_time,
            "status": self.status,
            "created_at": self.created_at,
        }