# Authentication

**Authentication** is the process of verifying the identity of a user or system to ensure they are who they claim to be.
- In the authentication process, a user’s identity is verified to ensure they are who they claim to be.
- Authentication is performed before the authorization process
- It needs usually the user's login details.
- Generally, transmit information through an **ID Token**.

**Authorization** is the process of determining and granting access rights to an authenticated user or system.
- In this process, a user’s identity is verified to ensure they are who they claim to be.
- Authorization is performed after the authentication process
- It requires the user’s privileges or security levels.
- Generally, transmit information through an **Access Token**.

---

# OAuth 2.0
Open Authorization - designed to allow a website or application to access resources hosted by other web apps on behalf of a user.
OAuth 2.0 is an authorization protocol and NOT an authentication protocol - use **Access Token**

## Roles
- Resource Owner
- Client
- Authorization Server
- Resource Server

## Access Tokens and Authorization Code
- The OAuth 2 Authorization server may not directly return an Access Token after the Resource Owner has authorized access. 
- Instead, and for better security, an **Authorization Code** may be returned, which is then exchanged for an **Access Token**. 
- In addition, the Authorization server may also issue a **Refresh Token**(Long expiry time, need to store securely) with the Access Token. 

## Working
- Client Request authorization from the Authorization server with credentials
- Authorization server authenticates the client
- Resource owner interacts with the Authorization server to grant access
- Authorization server redirects back to the Client with Auth code/Access token/Refersh token
- Client requests access to the resource from the Resource server

## Grant Types
- Authorization Code grant
- Implicit Grant
- Authorization Code Grant with Proof Key for Code Exchange (PKCE)
- Resource Owner Credentials Grant Type
- Client Credentials Grant Type
- Device Authorization Flow
- Refresh Token Grant

---

# JSON Web Token (JWT)
Secure way to send information between a client and a server

**Cryptographic methods**
- HMAC (Hash-based Message Authentication Code)
- RSA or ECDSA (Asymmetric cryptographic algorithms)

## JWT Structure
Three parts, separated by dots (.)
`Header. Payload. Signature`

- **Header**: Contains metadata about the token, such as the algorithm used for signing.
- **Payload**: Stores the claims, i.e., data being transmitted.
- **Signature**: Ensures the token's integrity and authenticity.

**Examples**
```
-- Header
{
    "alg": "HS256",
    "typ": "JWT"
}

-- Payload
{
    "userId": 123,
    "role": "admin",
    "exp": 1672531199
}

-- Signature
HMACSHA256(
    base64UrlEncode(header) + "." + base64UrlEncode(payload),
    secret
)
```

**Final JWT token** - Joining the Header, Payload and Signature via a dot

## Working
**Base64URL** encoding
- Login Request
- Server Generates JWT
- Returns JWT
- Further Requests with JWT

## Security Considerations
- Use HTTPS
- Set Expiration Time
- Use Secure Storage
- Verify Signature

---

