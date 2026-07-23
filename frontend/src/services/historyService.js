import api from "./api";

// Get all history
export const getHistory = () => {
  return api.get("/history/");
};

// Save history
export const saveHistory = (data) => {
  return api.post("/history/", data);
};

// Delete one history item
export const deleteHistory = (historyId) => {
  return api.delete(`/history/${historyId}`);
};

// Clear all history
export const clearHistory = () => {
  return api.delete("/history/");
};