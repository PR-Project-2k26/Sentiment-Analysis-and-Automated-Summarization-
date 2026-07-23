import { useEffect, useState } from "react";
import DashboardLayout from "../../components/Layout/DashboardLayout";

import HistoryList from "../../components/History/HistoryList";

import {
  getHistory,
  deleteHistory,
  clearHistory,
} from "../../services/historyService";

const History = () => {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      setLoading(true);

      const response = await getHistory();

      setHistory(response.data.history);
    } catch (error) {
      console.error("Failed to fetch history", error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteHistory(id);

      fetchHistory();
    } catch (error) {
      console.error(error);
    }
  };

  const handleClearAll = async () => {
    const confirmDelete = window.confirm(
      "Are you sure you want to clear all history?"
    );

    if (!confirmDelete) return;

    try {
      await clearHistory();

      fetchHistory();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <DashboardLayout>
      <div className="space-y-8">

        {/* Header */}

        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-white">
              History
            </h1>

            <p className="mt-2 text-zinc-400">
              View all AI analyses across Resume, PDF,
              Video, Audio and Text modules.
            </p>
          </div>

          <button
            onClick={handleClearAll}
            className="rounded-lg bg-red-600 px-5 py-2 text-white hover:bg-red-700"
          >
            Clear All
          </button>
        </div>

        {/* Loading */}

        {loading ? (
          <div className="text-center text-zinc-400">
            Loading History...
          </div>
        ) : (
          <HistoryList
            history={history}
            onDelete={handleDelete}
          />
        )}

      </div>
    </DashboardLayout>
  );
};

export default History;