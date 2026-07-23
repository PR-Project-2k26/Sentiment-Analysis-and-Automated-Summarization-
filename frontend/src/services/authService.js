import api from "./api";

export const loginUser = (data) => {
  return api.post("/auth/login", data);
};

export const registerUser = (data) => {
  return api.post("/auth/register", data);
};

export const forgotPassword = (email) => {
  return api.post("/auth/forgot-password", { email });
};