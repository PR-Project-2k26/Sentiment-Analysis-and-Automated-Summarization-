import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { registerUser } from "../../services/authService";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";
import Divider from "../../components/Authentication/Divider";
import SocialButtons from "../../components/Authentication/SocialButtons";

const Register = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
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

  const handleRegister = async (e) => {
    e.preventDefault();

    setMessage("");

    try {
      setLoading(true);

      const response = await registerUser(formData);

      setIsError(false);
      setMessage(response.data.message);

      setTimeout(() => {
        navigate("/login");
      }, 1500);

    } catch (error) {
      setIsError(true);
      setMessage(
        error.response?.data?.message || "Registration failed."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthLayout>
      <AuthCard>
        <form onSubmit={handleRegister}>
          <AuthHeader
            title="Create Account 🚀"
            subtitle="Join SummarAI and start using AI-powered tools."
          />

          {message && (
            <div
              className={`mb-4 rounded-lg border p-3 text-sm ${
                isError
                  ? "border-red-500 bg-red-500/10 text-red-400"
                  : "border-green-500 bg-green-500/10 text-green-400"
              }`}
            >
              {message}
            </div>
          )}

          <AuthInput
            label="Full Name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Enter your full name"
          />

          <AuthInput
            label="Email"
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter your email"
          />

          <PasswordInput
            name="password"
            value={formData.password}
            onChange={handleChange}
          />

          <div className="mb-6">
            <label className="flex items-center gap-2 text-sm text-gray-400">
              <input type="checkbox" required />
              I agree to the Terms & Conditions
            </label>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Creating Account..." : "Create Account"}
          </button>
        </form>

        <Divider />

        <SocialButtons />

        <p className="mt-8 text-center text-gray-400">
          Already have an account?{" "}
          <Link
            to="/login"
            className="font-medium text-blue-500 hover:text-blue-400"
          >
            Login
          </Link>
        </p>
      </AuthCard>
    </AuthLayout>
  );
};

export default Register;