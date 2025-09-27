# API

## API design

- API design is the process of making intentional decisions about how an API will expose data and functionality.
- API's endpoints, methods, and resources in a standardized specification format.

## Approaches

- Inside-out API design
- Outside-in API design
- Agile API design

## Key Stages

- Determine what the API is intended to do
- Define the API contract with a specification
- Validate your assumptions with mocks and tests
- Document the API

## API Design Patterns

- Request-response
- Pagination
- Rate limiting
- API authentication and authorization
- Webhooks

## What makes an API RESTfull?

- Standard HTTP Methods - Get, Post..
- JSON Output (Standard Data Format) or XML
- Client-Server completely separate
- Stateless - It should not store previous client requests, and it should not respond to a request based on the previous request.
- Resource-Based (Universal Resource Locator/Identifier - URL)

---

# HATEOAS

- **Hypermedia as the Engine of Application State**
- Client-side needs minimal knowledge about how to interact with a server
- With traditional, non-HATEOAS based API systems, the API endpoints need to be hard-coded within the client-side application.
