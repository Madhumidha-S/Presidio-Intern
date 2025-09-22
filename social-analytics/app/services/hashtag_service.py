from sqlalchemy.orm import Session
from app.models.hashtag import Hashtag
from app.schemas.hashtag_schema import HashtagCreate

def get_hashtags(db: Session):
    return db.query(Hashtag).all()

def create_hashtag(hashtag_data: HashtagCreate, db: Session):
    hashtag = Hashtag(**hashtag_data.dict())
    db.add(hashtag)
    db.commit()
    db.refresh(hashtag)
    return hashtag

def delete_hashtag(hashtag_id: int, db: Session):
    hashtag = db.query(Hashtag).filter(Hashtag.id == hashtag_id).first()
    if not hashtag:
        return {"error": f"Hashtag with id {hashtag_id} not found"}
    db.delete(hashtag)
    db.commit()
    return {"message": f"Hashtag {hashtag_id} deleted"}
