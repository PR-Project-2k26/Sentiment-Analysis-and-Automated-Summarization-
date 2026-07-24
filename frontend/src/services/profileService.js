import api from "./api";

export const getProfile = () => {
  return api.get("/auth/profile");
};

export const updateProfile = (data) => {
  return api.put("/auth/profile", data);
};