import { Trash2, Clock, Calendar } from "lucide-react";

const HistoryCard = ({ item, onDelete }) => {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-5 shadow-sm hover:border-blue-500 transition-all">
      <div className="flex items-start justify-between">
        <div>
          <h3 className="text-lg font-semibold text-white">
            {item.file_name}
          </h3>

          <p className="mt-1 text-blue-400 text-sm">
            {item.module}
          </p>
        </div>

        <button
          onClick={() => onDelete(item.id)}
          className="rounded-lg p-2 hover:bg-red-500/20"
        >
          <Trash2 className="h-5 w-5 text-red-400" />
        </button>
      </div>

      <p className="mt-4 text-sm text-zinc-300 line-clamp-3">
        {item.summary}
      </p>

      <div className="mt-5 flex items-center gap-6 text-sm text-zinc-400">
        <div className="flex items-center gap-2">
          <Clock size={16} />
          {item.processing_time}s
        </div>

        <div className="flex items-center gap-2">
          <Calendar size={16} />
          {new Date(item.created_at).toLocaleString()}
        </div>
      </div>
    </div>
  );
};

export default HistoryCard;