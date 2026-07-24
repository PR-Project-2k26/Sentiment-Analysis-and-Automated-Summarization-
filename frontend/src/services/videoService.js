import api from "./api";

export const uploadVideo = async (videoFile) => {
  const formData = new FormData();

  formData.append("video", videoFile);

  const response = await api.post("/video/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};