const express = require("express");
const cookieParser = require("cookie-parser");
require("dotenv").config();

const routes = require("./routes");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser(process.env.COOKIE_SECRET));

app.use("/", routes);

const PORT = process.env.PORT1 || 3000;
app.listen(PORT, () => console.log(`User Service running on port ${PORT}`));
