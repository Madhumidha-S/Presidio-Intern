const express = require("express");
const router = express.Router();
const courseController = require("../controllers/courseController");
const auth = require("../middleware/authMiddleware");
const roleCheck = require("../middleware/roleMiddleware");

const STUDENT = 3,
  TEACHER = 2,
  ADMIN = 1;

const combinedRoles = [TEACHER, ADMIN];

router.get("/", auth, courseController.getCourses);
router.post("/", auth, roleCheck(combinedRoles), courseController.createCourse);
router.post("/enroll", auth, roleCheck([STUDENT]), courseController.enroll);
router.post(
  "/assignment",
  auth,
  roleCheck(combinedRoles),
  courseController.createAssignment
);
router.post(
  "/submit",
  auth,
  roleCheck([STUDENT]),
  courseController.submitAssignment
);
router.get("/assignments", auth, courseController.getAssignments);
router.get(
  "/submissions/:assignment_id",
  auth,
  roleCheck(combinedRoles),
  courseController.getSubmissions
);

module.exports = router;

/**
 * @swagger
 * /course:
 *   get:
 *     summary: Get all courses
 *     tags: [Courses]
 *     responses:
 *       200:
 *         description: List of courses
 */
router.get("/", auth, courseController.getCourses);

/**
 * @swagger
 * /course:
 *   post:
 *     summary: Create a new course
 *     tags: [Courses]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               title:
 *                 type: string
 *               description:
 *                 type: string
 *               category:
 *                 type: string
 *     responses:
 *       201:
 *         description: Course created
 *       403:
 *         description: Forbidden
 */
router.post("/", auth, roleCheck(combinedRoles), courseController.createCourse);

/**
 * @swagger
 * /assignment:
 *   post:
 *     summary: Create a new assignment
 *     tags: [Assignments]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               course_id:
 *                 type: integer
 *               title:
 *                 type: string
 *               description:
 *                 type: string
 *               due_date:
 *                 type: string
 *                 format: date-time
 *                 example: "2025-10-15T23:59:00Z"
 *     responses:
 *       201:
 *         description: Assignment created successfully
 *       400:
 *         description: Invalid input
 */

/**
 * @swagger
 * /submit:
 *   post:
 *     summary: Submit an assignment
 *     tags: [Submissions]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               assignment_id:
 *                 type: integer
 *                 example: 3
 *     responses:
 *       201:
 *         description: Submission successful
 *       400:
 *         description: Already submitted or invalid
 */
