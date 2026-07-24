import api from "./api";

export const analyzeResume = async (file, jobDescription) => {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("jobDescription", jobDescription);

  const response = await api.post("/resume/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};