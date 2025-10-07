# Smart Learning Platform – Frontend

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Folder Structure](#folder-structure)  
5. [Core Components](#core-components)  
   - [Authentication & Role Management](#authentication--role-management)  
   - [Dashboard Views](#dashboard-views)  
   - [Course & Enrollment Flow](#course--enrollment-flow)  
   - [Analytics Integration](#analytics-integration)  
6. [Backend Integration](#backend-integration)  
7. [Installation & Setup](#installation--setup)

---

## Project Overview

The **Smart Learning Platform Frontend** provides a responsive and role-based interface for students, teachers, and administrators.  
It connects to a Node.js + Express backend through **REST APIs** using **Axios** and handles **cross-origin communication** via **CORS**.

This frontend system focuses on modular design, seamless navigation, and real-time data synchronization.  
It enables users to manage courses, view dashboards, submit assignments, and visualize analytics.

---

## Features

- **Role-Based Dashboards:** Dynamic UIs for Students, Teachers, and Admins  
- **Authentication System:** JWT-based login integrated via Context API  
- **Course Management:** Display, create, and enroll in courses  
- **Admin Analytics:** Graphical insights into platform data  
- **Axios-Powered API Calls:** Optimized and modular API communication  
- **Global State Management:** Context-based auth and user handling  
- **CORS Integration:** Secure communication with backend APIs  
- **Error Handling:** Graceful fallbacks and clear user alerts  
- **Responsive UI:** Works seamlessly across all screen sizes  

---

## Tech Stack

- **Framework:** React.js (with Vite)
- **Routing:** React Router DOM
- **State Management:** React Context API
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios  
- **Data Visualization:** Recharts (for analytics)  
- **Authentication:** JWT-based  
- **Backend Communication:** CORS-enabled Express APIs  

---

## Folder Structure

```
frontend/
│
├── src/
│   ├── components/
│   │   ├── DashboardLayout.jsx
│   │   ├── Navbar.jsx
│   │   ├── Sidebar.jsx
│   │   ├── Cards/
│   │   ├── Charts/
│   │   └── Analytics/
│   │
│   ├── context/
│   │   ├── AuthContext.js
│   │   └── AuthProvider.js
│   │
│   ├── services/
│   │   ├── axiosUser.js
│   │   ├── axiosCourse.js
│   │   └── axiosAnalytics.js
│   │
│   ├── pages/
│   │   ├── LoginPage.jsx
│   │   ├── RegisterPage.jsx
│   │   ├── Dashboard.jsx
│   │   ├── Courses.jsx
│   │   └── NotFound.jsx
│   │
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.css
│   └── router.js
│
├── package.json
├── vite.config.js
└── README.md
```

---

## Core Components

### Authentication & Role Management

- **Login and Registration:** Secure login integrated with backend using Axios (`/user/login`, `/user/register`)  
- **JWT Handling:** Tokens are stored in React Context for maintaining session state  
- **Role-Based Navigation:** Redirects users to dashboards (`/admin`, `/teacher`, `/student`) based on their role_id  
- **Protected Routes:** Only authenticated users can access core modules  

---

### Dashboard Views

Each user type has a dedicated dashboard layout:

- **Admin Dashboard:** Displays system statistics, user analytics, and global summaries  
- **Teacher Dashboard:** Lists teacher-owned courses, enrolled students, and allows new course creation  
- **Student Dashboard:** Displays enrolled courses, progress details, and submission status  

Each dashboard shares a **Navbar** and **Sidebar** component for consistent navigation.

---

### Course & Enrollment Flow

- **Course Listing:** Fetches data via `GET /courses`  
- **Course Details:** Displays details like instructor, duration, and category  
- **Enrollments:**  
  - Students can enroll in available courses using `POST /courses/:id/enroll`  
  - Teachers can create new courses with `POST /courses`  
- **Real-time Updates:** Changes reflect dynamically without manual page refresh  

---

### Analytics Integration

Accessible only to **Admins**, analytics data is fetched from `/analytics` endpoint.

- **Visualizations:** Age distribution, teacher-student ratios, and total summary stats  
- **Charts:** Implemented using **Recharts**  
- **Endpoints Used:**  
  - `GET /analytics` → Returns summary, ageStats, teacherStats  

---

## Backend Integration

The frontend communicates with the backend securely using **Axios** and **CORS**.

Example configuration:

```javascript
// src/services/axiosUser.js
import axios from "axios";

const userApi = axios.create({
  baseURL: "http://localhost:3000/user",
  withCredentials: true,
});

export default userApi;
```
- CORS is enabled on the backend to allow requests from the frontend origin (http://localhost:5173).
- Axios handles all HTTP requests, with dedicated files for each domain (user, courses, analytics).
- Error Handling: Responses are intercepted globally to catch and alert validation or server issues.

---
### Installation & Setup

1. Clone the Repository
```
git clone https://github.com/Madhumidha-S/Presidio-Intern.git
git checkout challenge3
cd smart-learning-frontend
```

2. Install Dependencies
`npm install`

3. Configure Environment Variables

4. Run the Development Server
`npm run dev`

5. Access the App
Visit http://localhost:5173 in your browser.