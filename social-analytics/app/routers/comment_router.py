from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import comment_service
from app.core.db import get_db
from app.schemas.comment_schema import CommentCreate, CommentResponse
from typing import List

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.get("/post/{post_id}", response_model=List[CommentResponse])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return comment_service.get_comments_by_post(post_id, db)

@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return comment_service.create_comment(comment, db)

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return comment_service.delete_comment(comment_id, db)
