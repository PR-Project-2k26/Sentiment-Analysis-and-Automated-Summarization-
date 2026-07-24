import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { loginUser } from "../../services/authService";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";
import AuthFooter from "../../components/Authentication/AuthFooter";

const Login = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [isError, setIsError] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    setMessage("");

    try {
      setLoading(true);

      const response = await loginUser(formData);

      localStorage.setItem("token", response.data.token);

      if (response.data.user) {
        localStorage.setItem(
          "user",
          JSON.stringify(response.data.user)
        );
      }

      setIsError(false);
      setMessage("Login successful!");

      setTimeout(() => {
        const redirect = sessionStorage.getItem(
          "redirectAfterLogin"
        );

        if (redirect) {
          sessionStorage.removeItem("redirectAfterLogin");
          navigate(redirect);
        } else {
          navigate("/dashboard");
        }
      }, 1000);
    } catch (error) {
      setIsError(true);

      setMessage(
        error.response?.data?.message ||
          "Invalid email or password."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthLayout>
      <AuthCard>

        <AuthHeader
          subtitle="Welcome back! Enter your credentials to access your account."
        />

        <form onSubmit={handleLogin} className="space-y-5">

          {message && (
            <div
              className={`rounded-lg border p-3 text-sm ${
                isError
                  ? "border-red-500 bg-red-500/10 text-red-400"
                  : "border-green-500 bg-green-500/10 text-green-400"
              }`}
            >
              {message}
            </div>
          )}

          <AuthInput
            label="Email Address"
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="john@example.com"
          />

          <PasswordInput
            name="password"
            value={formData.password}
            onChange={handleChange}
          />

          <div className="flex items-center justify-between text-sm">

            <label className="flex items-center gap-2 text-gray-400">
              <input
                type="checkbox"
                className="rounded border-white/20 bg-transparent"
              />
              Remember me
            </label>

            <Link
              to="/forgot-password"
              className="text-blue-500 hover:text-blue-400"
            >
              Forgot password?
            </Link>

          </div>

          <button
            type="submit"
            disabled={loading}
            className="mt-2 w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition duration-200 hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Signing In..." : "Sign In"}
          </button>

        </form>

        <AuthFooter />

      </AuthCard>
    </AuthLayout>
  );
};

export default Login;