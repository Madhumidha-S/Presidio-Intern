const express = require("express");
const courseRouter = require("./courseRouter");
const router = express.Router();
router.use("/course", courseRouter);
module.exports = router;
