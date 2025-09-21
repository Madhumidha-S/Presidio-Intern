from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment

def most_engaged_users(db: Session, limit: int = 10):
    q = (
        db.query(
            User.id,
            User.username,
            func.count(Comment.id).label("num_comments"),
            func.count(Post.id).label("num_posts"),
            (func.count(Comment.id) + 0.2 * func.count(Post.id)).label("engagement_score")
        )
        .join(Post, Post.user_id == User.id)
        .outerjoin(Comment, Comment.post_id == Post.id)
        .group_by(User.id)
        .order_by(func.count(Comment.id).desc())
        .limit(limit)
    )
    return q.all()
