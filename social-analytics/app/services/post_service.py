from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post_schema import PostCreate

def get_posts(db: Session):
    return db.query(Post).all()

def get_post(post_id: int, db: Session):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(post_data: PostCreate, db: Session):
    post = Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def delete_post(post_id: int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return {"error": f"Post with id {post_id} not found"}
    db.delete(post)
    db.commit()
    return {"message": f"Post {post_id} deleted"}
