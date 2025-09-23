# Middleware

Middleware is a software tools that act as an intermediary between different applications, systems, or services, facilitating their communication and interaction.

- Handles data translation, message queuing, authentication, and connectivity
- It first controls access to different back-end resources. A connection pool could be established by a middleware component to enable quick and easy access to a well-liked back-end database.
- In load balancing, transaction management, and concurrent processing, middleware is crucial.
- Middleware software is capable of executing logic according to the client's request.
- Two requirements: a Secure Connection(SSL) and Authentication.

**Examples**

- Database middleware
- Web server middleware
- Message-oriented middleware

```
-- Syntax
app.use((req, res, next) => {
    console.log('Middleware executed');
    next();
});
```

## Categories

- Platform middleware
- Enterprise application integration middleware

## Types

- Remote Procedure Call (RPC)
- Messaging middleware
- Embedded middleware
- API middleware
- Asynchronous data streaming middleware
- Transaction or transactional middleware
- Error-handling Middleware
- Built-in Middleware
- Third-party Middleware(morgan)

## Difference between Application Level and Router Level Middleware

Application-level middleware is like a personal assistant that helps out with every incoming request.

```
app.use(express.json()); 
app.use((req, res, next) => {
  console.log('Request received:', req.method, req.url);
  next();
});
```

Router-level middleware is more specialized - it only applies to particular routing paths you choose.

```
const router = express.Router();
router.use((req, res, next) => {
  console.log('Router-specific middleware');
  next();
});
router.get('/dashboard', (req, res) => {
  res.send('Dashboard Page');
});
app.use('/user', router);
```

## Error Handling Middleware
```
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});
```

## Built-in Middleware
```
app.use(express.static('public'));
app.use(express.json());
```

## Middleware Chaining

Middleware can be chained from one to another, Hence creating a chain of functions that are executed in order. The last function sends the response back to the browser. So, before sending the response back to the browser the different middleware processes the request.

`next()` - responsible for this.

```
-- Syntax
const middleware1 = (req, res, next) => {
// Tasks
next();
};
const middleware2 = (req, res, next) => {
// Tasks
next();
};
app.get('/example', middleware1, middleware2, (req, res) => {
  // Route handler
});
```