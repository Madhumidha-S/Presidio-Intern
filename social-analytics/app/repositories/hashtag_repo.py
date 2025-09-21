from sqlalchemy.orm import Session
from sqlalchemy import select, update
from app.models.hashtag import Hashtag
from app.models.post_hashtag import PostHashtag

def get_or_create_hashtag(db: Session, tag: str):
    h = db.query(Hashtag).filter(Hashtag.tag == tag).one_or_none()
    if h:
        return h
    h = Hashtag(tag=tag, count=0)
    db.add(h)
    db.flush()
    return h

def increment_hashtag_count(db: Session, hashtag_id: int, delta: int = 1):
    db.execute(
        update(Hashtag).where(Hashtag.id == hashtag_id).values(count=Hashtag.count + delta)
    )

def get_top_hashtags(db: Session, limit: int = 10):
    return db.query(Hashtag).order_by(Hashtag.count.desc()).limit(limit).all()
