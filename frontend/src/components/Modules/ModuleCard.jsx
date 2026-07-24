import { useNavigate } from "react-router-dom";

const ModuleCard = ({ title, description, emoji, link }) => {
  const navigate = useNavigate();

  const handleModuleClick = () => {
    const token = localStorage.getItem("token");

    if (token) {
      navigate(link);
    } else {
      // Save the page the user wanted
      sessionStorage.setItem("redirectAfterLogin", link);

      navigate("/login");
    }
  };

  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-md transition-all duration-300 hover:-translate-y-2 hover:border-blue-500/40 hover:bg-white/10">

      {/* Emoji */}
      <div className="text-4xl">
        {emoji}
      </div>

      {/* Title */}
      <h3 className="mt-5 text-2xl font-bold text-white">
        {title}
      </h3>

      {/* Description */}
      <p className="mt-3 text-gray-400">
        {description}
      </p>

      {/* Button */}
      <button
        onClick={handleModuleClick}
        className="mt-6 inline-block rounded-lg bg-blue-600 px-5 py-2 font-medium text-white transition hover:bg-blue-700"
      >
        Open Module →
      </button>

    </div>
  );
};

export default ModuleCard;