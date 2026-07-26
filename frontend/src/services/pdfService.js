import api from "./api";

export const summarizePDF = async (file) => {

  const formData = new FormData();

  formData.append("pdf", file);

  const response = await api.post(
    "/pdf/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};