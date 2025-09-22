from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment_schema import CommentCreate

def get_comments_by_post(post_id: int, db: Session):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def create_comment(comment_data: CommentCreate, db: Session):
    comment = Comment(**comment_data.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def delete_comment(comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        return {"error": f"Comment with id {comment_id} not found"}
    db.delete(comment)
    db.commit()
    return {"message": f"Comment {comment_id} deleted"}
