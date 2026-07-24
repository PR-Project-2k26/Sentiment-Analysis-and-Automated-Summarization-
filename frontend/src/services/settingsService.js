import api from "./api";

export const changePassword = async (passwordData) => {
  return await api.put("/auth/change-password", passwordData);
};