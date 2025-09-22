from sqlalchemy.orm import Session
from app.models.post_hashtag import PostHashtag
from app.models.hashtag import Hashtag
from app.schemas.post_hashtag_schema import PostHashtagCreate

def link_post_hashtag(data: PostHashtagCreate, db: Session):
    existing = db.query(PostHashtag).filter(
        PostHashtag.post_id == data.post_id,
        PostHashtag.hashtag_id == data.hashtag_id
    ).first()

    if existing:
        return existing

    link = PostHashtag(**data.dict())
    db.add(link)
    hashtag = db.query(Hashtag).filter(Hashtag.id == data.hashtag_id).first()
    if hashtag:
        hashtag.count += 1

    db.commit()
    db.refresh(link)
    return link

def unlink_post_hashtag(post_id: int, hashtag_id: int, db: Session):
    link = db.query(PostHashtag).filter(
        PostHashtag.post_id == post_id,
        PostHashtag.hashtag_id == hashtag_id
    ).first()

    if not link:
        return {"error": "Link does not exist"}

    db.delete(link)

    hashtag = db.query(Hashtag).filter(Hashtag.id == hashtag_id).first()
    if hashtag and hashtag.count > 0:
        hashtag.count -= 1

    db.commit()
    return {"message": f"Hashtag {hashtag_id} unlinked from Post {post_id}"}

def get_post_hashtags(post_id: int, db: Session):
    return db.query(PostHashtag).filter(PostHashtag.post_id == post_id).all()

def get_hashtag_posts(hashtag_id: int, db: Session):
    return db.query(PostHashtag).filter(PostHashtag.hashtag_id == hashtag_id).all()
