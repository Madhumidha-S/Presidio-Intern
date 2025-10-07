// import React from "react";
// import {
//   BrowserRouter as Router,
//   Routes,
//   Route,
//   Navigate,
// } from "react-router-dom";
// import Login from "./pages/Login";
// import DashboardStudent from "./pages/StudentDashboard";
// import DashboardTeacher from "./pages/TeacherDashboard";
// import DashboardAdmin from "./pages/AdminDashboard";
// import ProtectedRoute from "./routes/ProtectedRoute";
// import { useAuth } from "./context/AuthContext";
// import { StrictMode } from "react";
// import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
// import { ToastContainer } from "react-toastify";
// import Courses from "./pages/Courses";
// import "react-toastify/dist/ReactToastify.css";
// // import MyCourses from "./pages/MyCourses";

// const AppRoutes = () => {
//   const { user } = useAuth();

//   const getDashboard = () => {
//     if (!user) return <Navigate to="/login" />;
//     switch (user.role_id) {
//       case 1:
//         return <Navigate to="/admin" />;
//       case 2:
//         return <Navigate to="/teacher" />;
//       case 3:
//         return <Navigate to="/student" />;
//       default:
//         return <Navigate to="/login" />;
//     }
//   };

//   return (
//     <Routes>
//       <Route path="/login" element={<Login />} />
//       <Route path="/dashboard" element={getDashboard()} />

//       <Route
//         path="/student"
//         element={
//           <ProtectedRoute allowedRoles={[3]}>
//             <DashboardStudent />
//           </ProtectedRoute>
//         }
//       />
//       <Route
//         path="/teacher"
//         element={
//           <ProtectedRoute allowedRoles={[2]}>
//             <DashboardTeacher />
//           </ProtectedRoute>
//         }
//       />
//       <Route
//         path="/admin"
//         element={
//           <ProtectedRoute allowedRoles={[1]}>
//             <DashboardAdmin />
//           </ProtectedRoute>
//         }
//       />
//       <Route
//         path="/courses"
//         element={
//           <ProtectedRoute>
//             <Courses />
//           </ProtectedRoute>
//         }
//       />

//       <Route path="*" element={<Navigate to="/login" />} />
//       {/* <Route path="/courses" element={<MyCourses />} /> */}
//     </Routes>
//   );
// };

// const queryClient = new QueryClient();

// export default function App() {
//   return (
//     <div className="w-screen h-screen overflow-hidden">
//       <Router>
//         <StrictMode>
//           <QueryClientProvider client={queryClient}>
//             {/*  <AuthProvider> */}
//             <AppRoutes />
//             <ToastContainer position="top-right" />
//             {/* </AuthProvider> */}
//           </QueryClientProvider>
//         </StrictMode>
//       </Router>
//     </div>
//   );
// }

import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Login from "./pages/Login";
import DashboardStudent from "./pages/StudentDashboard";
import DashboardTeacher from "./pages/TeacherDashboard";
import DashboardAdmin from "./pages/AdminDashboard";
import Courses from "./pages/Courses";
import ManageTeachersTab from "./pages/ManageTeacher";
import ProtectedRoute from "./routes/ProtectedRoute";
import { AuthProvider, useAuth } from "./context/AuthContext";
import { StrictMode } from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const AppRoutes = () => {
  const { user } = useAuth();

  const getDashboard = () => {
    if (!user) return <Navigate to="/login" />;
    switch (user.role_id) {
      case 1:
        return <Navigate to="/admin" />;
      case 2:
        return <Navigate to="/teacher" />;
      case 3:
        return <Navigate to="/student" />;
      default:
        return <Navigate to="/login" />;
    }
  };

  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={getDashboard()} />

      <Route
        path="/teacher"
        element={
          <ProtectedRoute allowedRoles={[2]}>
            <DashboardTeacher />
          </ProtectedRoute>
        }
      />

      <Route
        path="/teacher/courses"
        element={
          <ProtectedRoute allowedRoles={[2]}>
            <Courses />
          </ProtectedRoute>
        }
      />

      <Route
        path="/student"
        element={
          <ProtectedRoute allowedRoles={[3]}>
            <DashboardStudent />
          </ProtectedRoute>
        }
      />

      <Route
        path="/student/courses"
        element={
          <ProtectedRoute allowedRoles={[3]}>
            <Courses />
          </ProtectedRoute>
        }
      />

      <Route
        path="/admin"
        element={
          <ProtectedRoute allowedRoles={[1]}>
            <DashboardAdmin />
          </ProtectedRoute>
        }
      />

      <Route
        path="/admin/teachers"
        element={
          <ProtectedRoute allowedRoles={[1]}>
            <ManageTeachersTab />
          </ProtectedRoute>
        }
      />

      <Route path="*" element={<Navigate to="/login" />} />
    </Routes>
  );
};

const queryClient = new QueryClient();

export default function App() {
  return (
    <div className="w-screen h-screen overflow-hidden">
      <Router>
        <StrictMode>
          <QueryClientProvider client={queryClient}>
            <AuthProvider>
              <AppRoutes />
              <ToastContainer position="top-right" />
            </AuthProvider>
          </QueryClientProvider>
        </StrictMode>
      </Router>
    </div>
  );
}
