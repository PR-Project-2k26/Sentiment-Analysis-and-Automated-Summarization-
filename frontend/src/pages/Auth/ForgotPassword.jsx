import { Link } from "react-router-dom";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";

const ForgotPassword = () => {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Forgot Password?"
          subtitle="Enter your email to receive a password reset link."
        />

        <AuthInput
          label="Email"
          type="email"
          placeholder="Enter your email"
        />

        <button className="mt-4 w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700">
          Send Reset Link
        </button>

        <p className="mt-8 text-center text-gray-400">
          Remember your password?{" "}
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

export default ForgotPassword;