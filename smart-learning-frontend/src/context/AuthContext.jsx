import React, { createContext, useContext, useState, useEffect } from "react";
import userApi from "../api/axiosUser";
import Cookies from "js-cookie";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkUser = async () => {
      const token = Cookies.get("token");
      if (!token) return setLoading(false);
      try {
        const res = await userApi.get("/profile");
        setUser(res.data.user);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    checkUser();
  }, []);

  const login = async (email, password) => {
    const res = await userApi.post("/login", { email, password });
    setUser(res.data.user);
  };

  const profile = async () => {
    const res = await userApi.get("/profile");
    setUser(res.data.user);
  };

  const logout = () => {
    Cookies.remove("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, loading, profile }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
