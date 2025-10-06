import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const ProtectedRoute = ({ children, allowedRoles }) => {
  const { user, loading } = useAuth();

  if (loading) return <p className="text-center mt-20">Loading...</p>;

  if (!user) return <Navigate to="/login" />;
  if (!allowedRoles.includes(user.role_id)) return <Navigate to="/login" />;

  return children;
};

export default ProtectedRoute;
