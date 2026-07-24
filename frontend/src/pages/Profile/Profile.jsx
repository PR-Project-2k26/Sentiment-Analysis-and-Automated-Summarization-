import { useEffect, useState } from "react";
import DashboardLayout from "../../components/Layout/DashboardLayout";
import { getProfile } from "../../services/profileService";

const Profile = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await getProfile();
        setUser(response.data.user);
      } catch (error) {
        console.error(error);
      }
    };

    fetchProfile();
  }, []);

  return (
    <DashboardLayout>
      <div className="mx-auto max-w-3xl">
        <div className="rounded-2xl border border-white/10 bg-white/5 p-8">
          <h1 className="mb-8 text-3xl font-bold text-white">
            👤 My Profile
          </h1>

          {!user ? (
            <div className="text-gray-400">Loading...</div>
          ) : (
            <div className="space-y-6">

              <div>
                <p className="text-sm text-gray-400">
                  Full Name
                </p>

                <p className="mt-2 text-xl font-semibold text-white">
                  {user.name}
                </p>
              </div>

              <div>
                <p className="text-sm text-gray-400">
                  Email
                </p>

                <p className="mt-2 text-xl font-semibold text-white">
                  {user.email}
                </p>
              </div>

              <div>
                <p className="text-sm text-gray-400">
                  Member Since
                </p>

                <p className="mt-2 text-xl font-semibold text-white">
                  {new Date(user.created_at).toLocaleDateString()}
                </p>
              </div>

            </div>
          )}
        </div>
      </div>
    </DashboardLayout>
  );
};

export default Profile;