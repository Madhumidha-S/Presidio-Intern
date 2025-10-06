import { NavLink } from "react-router-dom";
import { BookOpen, Home, LogOut } from "lucide-react";
import { useAuth } from "../context/AuthContext";

const Sidebar = ({ links }) => {
  const { logout } = useAuth();

  return (
    <div className="w-64 bg-white border-r border-gray-200 min-h-screen p-5 shadow-sm">
      <h1 className="text-2xl font-bold text-blue-600 mb-8">SmartLearn</h1>

      <nav className="space-y-3">
        {links.map((link) => (
          <NavLink
            key={link.to}
            to={link.to}
            className={({ isActive }) =>
              `flex items-center gap-3 px-4 py-2 rounded-lg text-gray-700 font-medium transition ${
                isActive ? "bg-blue-100 text-blue-700" : "hover:bg-gray-100"
              }`
            }
          >
            <BookOpen size={18} /> {link.label}
          </NavLink>
        ))}
      </nav>

      <button
        onClick={logout}
        className="mt-10 flex items-center gap-3 px-4 py-2 text-red-600 hover:bg-red-100 rounded-lg transition"
      >
        <LogOut size={18} /> Logout
      </button>
    </div>
  );
};

export default Sidebar;
