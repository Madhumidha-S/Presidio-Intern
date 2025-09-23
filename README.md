# Social Media Backend (FastAPI + PostgreSQL)

A backend project that implements core features of a social media app using **FastAPI** and **PostgreSQL**.  
It includes support for **Users**, **Posts**, **Comments** **Hashtags**, **Post-Hashtag**, **Hashtag Engine** and a **nested Comment parser** with recursion.

---

## Features

### Users

Users can create their profile.

### Posts

- Users can create and view posts.
- Each post can have multiple hashtags and comments.

### Hashtags

- Extract hashtags automatically from post content.
- Store hashtags in a separate table.
- Maintain **Post ↔ Hashtag** relations.
- Hashtag Engine:
  - Track hashtag frequencies across posts.
  - Suggest top 3 related hashtags with **>30% co-occurrence rate**.

### Comments

- Nested comments using `parent_id`.
- Recursive comment tree builder.
- Engagement depth calculation (number of nested replies).
- Viral comment chain detection with recursive backtracking.
- Optional **memoization** for performance.

### Post-Hashtags

It is the linking of a Hashtag to a post

### Hashtag Engine

- Track hashtag frequencies across posts
- Build hashtag recommendation engine that suggests top 3 related hashtags with >30% co-occurrence rate

### Nested Comment Parser

- Parse nested comment structures (recursive traversal)
- Calculate engagement depth (No of nested replies, ... etc) scores recursively
- Find viral comment chains using recursive backtracking

---

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Testing**: Postman / cURL

---

## API Endpoints

### Users

- `POST /users/` – Create user
- `GET /users/` – Get all users
- `GET /users/{user_id}` – Get user by ID
- `DELETE /users/{user_id}` – Delete user

### Posts

- `POST /posts/` – Create post
- `GET /posts/` – Get all posts
- `GET /posts/{post_id}` – Get post by ID
- `DELETE /posts/{post_id}` – Delete post

### Comments

- `POST /comments/` – Add comment
- `GET /comments/post/{post_id}` – Get comments for a post
- `GET /comments/thread/{post_id}` – Get nested comment thread
- `DELETE /comments/{comment_id}` – Delete comment

### Hashtags

- `GET /hashtags/` – Get all hashtags
- `GET /hashtags/trending` – Get trending hashtags

### Post-Hashtags

- `POST /post-hashtags/` – Link post to hashtags
- `GET /post-hashtags/{post_id}` – Get hashtags for a post

### Analytics

- `GET /analytics/hashtags/related/{tag}` – Get related hashtags (>30% co-occurrence)
- `GET /analytics/comments/engagement/{post_id}` – Analyze comment thread engagement

---

## Running Locally

1. Clone repo:

```
git clone https://github.com/yourusername/social-backend.git
cd social-backend
```

2. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure PostgreSQL in .env:
   DATABASE_URL=postgresql://username:password@localhost:5432/socialdb

5. Run FastAPI server:
   uvicorn app.main:app --reload

6. Open docs:
   http://127.0.0.1:8000/docs

7. Testing with Postman

## Future Improvements

- Add authentication (JWT).
- Support likes & shares.
- Real-time updates with WebSockets.
- Caching with Redis.
