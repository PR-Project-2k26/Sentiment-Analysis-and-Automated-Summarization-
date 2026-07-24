import api from "./api";

export const uploadAudio = async (audioFile) => {
  const formData = new FormData();

  formData.append("audio", audioFile);

  const response = await api.post("/audio/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};