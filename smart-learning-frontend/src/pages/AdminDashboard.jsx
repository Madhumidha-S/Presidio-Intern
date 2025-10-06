import DashboardLayout from "../components/DashboardLayout";

const AdminDashboard = () => {
  const links = [
    { to: "/admin", label: "Analytics" },
    { to: "/admin/courses", label: "Courses" },
  ];

  return (
    <DashboardLayout links={links}>
      <h1 className="text-2xl font-bold text-blue-700 mb-6">
        Analytics Overview
      </h1>

      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow border">
          <h2 className="text-gray-500 mb-2">Total Students</h2>
          <p className="text-3xl font-bold text-blue-600">240</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow border">
          <h2 className="text-gray-500 mb-2">Active Teachers</h2>
          <p className="text-3xl font-bold text-blue-600">18</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow border">
          <h2 className="text-gray-500 mb-2">Ongoing Courses</h2>
          <p className="text-3xl font-bold text-blue-600">35</p>
        </div>
      </div>
    </DashboardLayout>
  );
};

export default AdminDashboard;
