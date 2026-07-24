import api from "./api";

export const summarizeText = async (text, length = "Medium") => {
  const response = await api.post("/text/summarize", {
    text,
    length,
  });

  return response.data;
};