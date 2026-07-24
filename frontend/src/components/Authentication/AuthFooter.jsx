import { Link } from "react-router-dom";

const AuthFooter = () => {
  return (
    <div className="mt-8 border-t border-white/10 pt-6">
      <p className="text-center text-sm text-gray-400">
        Don't have an account?{" "}
        <Link
          to="/register"
          className="font-semibold text-blue-500 transition hover:text-blue-400"
        >
          Create Account
        </Link>
      </p>
    </div>
  );
};

export default AuthFooter;