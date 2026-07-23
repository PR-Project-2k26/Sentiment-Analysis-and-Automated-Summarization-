import api from "./api";

export const getProfile = async () => {
  const token = localStorage.getItem("token");

  return api.get("/auth/profile", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};