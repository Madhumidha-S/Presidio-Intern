from sqlalchemy.orm import Session
from app.models.post import Post
from app.repositories.hashtag_repo import get_or_create_hashtag, increment_hashtag_count
from app.models.post_hashtag import PostHashtag

def create_post_with_hashtags(db: Session, user_id: int, content: str, tags: list[str]):
    post = Post(user_id=user_id, content=content)
    db.add(post)
    db.flush() 
    try:
        for tag in tags:
            h = get_or_create_hashtag(db, tag)
            ph = PostHashtag(post_id=post.id, hashtag_id=h.id)
            db.add(ph)
            increment_hashtag_count(db, h.id, delta=1)
        db.commit()
        db.refresh(post)
        return post
    except Exception:
        db.rollback()
        raise
