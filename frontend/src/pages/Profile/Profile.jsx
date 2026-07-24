import { useEffect, useState } from "react";
import DashboardLayout from "../../components/Layout/DashboardLayout";
import {
  getProfile,
  updateProfile,
} from "../../services/profileService";

const Profile = () => {
  const [user, setUser] = useState(null);
  const [name, setName] = useState("");
  const [editing, setEditing] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      const response = await getProfile();

      setUser(response.data.user);
      setName(response.data.user.name);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    try {
      await updateProfile({
        name,
      });

      alert("Profile updated successfully!");

      setEditing(false);

      fetchProfile();
    } catch (error) {
      console.error(error);
      alert("Failed to update profile.");
    }
  };

  return (
    <DashboardLayout>
      <div className="mx-auto max-w-3xl">
        <div className="rounded-2xl border border-white/10 bg-white/5 p-8">

          <h1 className="mb-8 text-3xl font-bold text-white">
            👤 My Profile
          </h1>

          {loading ? (
            <div className="text-gray-400">
              Loading...
            </div>
          ) : (
            <div className="space-y-8">

              <div>
                <label className="text-sm text-gray-400">
                  Full Name
                </label>

                {editing ? (
                  <input
                    value={name}
                    onChange={(e) =>
                      setName(e.target.value)
                    }
                    className="mt-2 w-full rounded-xl border border-white/10 bg-[#111] p-3 text-white"
                  />
                ) : (
                  <p className="mt-2 text-2xl font-semibold text-white">
                    {user.name}
                  </p>
                )}
              </div>

              <div>
                <label className="text-sm text-gray-400">
                  Email
                </label>

                <p className="mt-2 text-xl font-semibold text-white">
                  {user.email}
                </p>
              </div>

              <div>
                <label className="text-sm text-gray-400">
                  Member Since
                </label>

                <p className="mt-2 text-xl font-semibold text-white">
                  {new Date(user.created_at).toLocaleDateString()}
                </p>
              </div>

              <div className="pt-4">

                {editing ? (
                  <button
                    onClick={handleSave}
                    className="rounded-xl bg-green-600 px-6 py-3 font-semibold text-white hover:bg-green-700"
                  >
                    Save Changes
                  </button>
                ) : (
                  <button
                    onClick={() => setEditing(true)}
                    className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white hover:bg-blue-700"
                  >
                    Edit Profile
                  </button>
                )}

              </div>

            </div>
          )}

        </div>
      </div>
    </DashboardLayout>
  );
};

export default Profile;