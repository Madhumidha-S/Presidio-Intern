const express = require("express");
const { signup, login, logout } = require("../controllers/userController");
const authMiddleware = require("../middleware/authMiddleware");
const roleMiddleware = require("../middleware/roleMiddleware");
const router = express.Router();

router.post("/signup", signup);
router.post("/login", login);
router.post("/logout", logout);

router.get("/profile", authMiddleware, (req, res) => {
  res.json({ message: "This is your profile", user: req.user });
});

router.get("/admin", authMiddleware, roleMiddleware([1]), (req, res) => {
  res.json({ message: "Welcome Admin!" });
});
router.get("/teacher", authMiddleware, roleMiddleware([2]), (req, res) => {
  res.json({ message: "Welcome Teacher!" });
});
router.get("/student", authMiddleware, roleMiddleware([3]), (req, res) => {
  res.json({ message: "Welcome Student!" });
});

module.exports = router;
