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
- Third-party Middleware

## Difference between Application Level and Router Level Middleware

Application-level middleware is like a personal assistant that helps out with every incoming request.
`app.use(params...);`

Router-level middleware is more specialized - it only applies to particular routing paths you choose.
`router.use(params...);`
