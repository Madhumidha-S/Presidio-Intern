# Smart Learning Platform

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Folder Structure](#folder-structure)
5. [Database Schema](#database-schema)
6. [Core Components](#core-components)
   - [Authentication](#authentication)
   - [Role-Based Access Control](#role-based-access-control-rbac)
   - [Course Management](#course-management)
   - [Assignments & Submissions](#assignments--submissions)
7. [Middleware & Logging](#middleware--logging)
8. [Installation & Setup](#installation--setup)
9. [API Documentation](#api-documentation)

---

## Project Overview

The **Smart Learning Platform** is a backend system that enables students to:

- Enroll in courses
- Submit assignments
- View personalized dashboards  
  And allows teachers to:
- Create & manage courses
- Manage assignments
- Track student performance

The system is designed to be **secure, scalable, cloud-ready**, and follows **modern backend practices** including JWT-based authentication, RBAC, middleware logging, and RESTful API design.

---

## Features

- **User Authentication:** JWT-based and session-based authentication
- **Role-Based Access Control:** Students, Teachers, Admin
- **Course Management:** CRUD operations for courses
- **Enrollment:** Students can enroll in courses
- **Assignments:** Teachers can create assignments; students can submit assignments
- **Analytics:** Admins can access protected analytics routes
- **REST API Features:** Pagination, filtering, sorting, HATEOAS links
- **Middleware:** Global logging, route-specific security, rate limiting
- **Logging:** Info-level logs for requests, error-level logs for failures

---

## Tech Stack

- **Backend:** Node.js, Express.js
- **Database:** PostgreSQL
- **Authentication:** JWT, Express session
- **Logging:** Winston
- **Rate Limiting:** Express Rate Limit middleware
- **Containerization:** Docker

---

## Folder Structure

```
smart-learning-platform/
│
├── user-service/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── utils/
│   ├── config.js
│   ├── index.js
│   ├── package.json
|   ├── package-lock.json
│   └── Dockerfile
│
├── course-service/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── utils/
│   ├── config.js
│   ├── index.js
│   ├── package.json
|   ├── package-lock.json
│   └── Dockerfile
│
├── .env
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

## Database Schema

- **Roles Table:** id, role_name (student, teacher, admin)
- **Users Table:** id, username, email, password, role_id, created_at
- **Courses Table:** id, title, description, category, rating, instructor_id, created_at
- **Enrollments Table:** id, user_id, course_id, enrolled_at
- **Assignments Table:** id, course_id, title, due_date
- **Submissions Table:** id, assignment_id, user_id, content, submitted_at, status

---

## Core Components

### Authentication

- JWT-Based Login: /auth/login
- Session-Based Login: /profile
- Secure password storage: bcrypt

### Role-Based Access Control (RBAC)

- Student: view/enroll courses, submit assignments
- Teacher: create/update courses & assignments
- Admin: access analytics routes

### Course Management

- GET /courses → Pagination, filtering, sorting
- POST /courses → Create course (Teacher/Admin)
- POST /courses/:id/enroll → Enroll student

### Assignments & Submissions

- POST /assignments/:id/submissions → Submit assignment
- GET /assignments/:id/submissions → Teacher views submissions

---

## Middleware & Logging

- Global Middleware: Logs method, path, timestamp for every request
- Route Middleware: Checks API key for /analytics
- Error Logging: Assignment submission failures logged at error-level

---

## Installation & Setup

Clone Repository
`git clone https://github.com/yourusername/smart-learning-backend.git`
cd smart-learning-backend

Install Dependencies

```
cd user-service && npm install
cd ../course-service && npm install
```

Setup PostgreSQL Database
Configure .env

Run Services

```
cd user-service && npm start
cd ../course-service && npm start
```

---

## API Documentation

- Documented using Swagger
- Browsable & testable via Swagger UI: /api-docs
