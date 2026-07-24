import config.db as database


class DashboardService:

    @staticmethod
    def get_dashboard_stats(user_id):
        history_collection = database.db["history"]

        history = list(history_collection.find({"user_id": user_id}))

        total = len(history)

        stats = {
            "Resume Analyzer": 0,
            "PDF Summarizer": 0,
            "Video Summarizer": 0,
            "Audio Summarizer": 0,
            "Text Summarizer": 0,
        }

        processing_time = 0
        recent_activity = []

        for item in history:
            module = item.get("module", "")

            if module in stats:
                stats[module] += 1

            processing_time += item.get("processing_time", 0)

            recent_activity.append({
                "id": str(item["_id"]),
                "module": module,
                "file_name": item.get("file_name"),
                "created_at": str(item.get("created_at")),
            })

        average_processing_time = (
            round(processing_time / total, 2)
            if total > 0
            else 0
        )

        recent_activity = sorted(
            recent_activity,
            key=lambda x: x["created_at"],
            reverse=True,
        )[:5]

        return {
            "totalAnalyses": total,
            "resume": stats["Resume Analyzer"],
            "pdf": stats["PDF Summarizer"],
            "video": stats["Video Summarizer"],
            "audio": stats["Audio Summarizer"],
            "text": stats["Text Summarizer"],
            "averageProcessingTime": average_processing_time,
            "recentActivity": recent_activity,
        }