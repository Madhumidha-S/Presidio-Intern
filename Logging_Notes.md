# Logging

From starting to debugging and adding new features, logs provide support by analyzing the data, and we can resolve bugs much easier and quicker by detecting errors as soon as they occur.

## Levels of logging

- error - Critical issues
- warn - Potential problems
- info - General info, status updates
- debug - Detailed info, mostly for development

## Methods

- console.log
- debug module
- Middleware (for HTTP frameworks)
- Winston package

## debug module

```
const debug = require("debug")("app:startup");
debug("Debugging info here...");
```

## Middleware

```
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});
```

## Winston Logger

```
const winston = require("winston");

const logger = winston.createLogger({
  level: "info",
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: "app.log" })
  ]
});

logger.info("Application started");
logger.error("An error occurred");

```
