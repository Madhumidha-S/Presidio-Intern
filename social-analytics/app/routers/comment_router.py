from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from app.schemas.comment_schema import CommentCreate, CommentResponse
from app.services.comment_service import CommentService
from app.core.db import get_db

router = APIRouter(
    prefix="/posts/{post_id}/comments",
    tags=["comments"]
)

def get_comment_service(db: Session = Depends(get_db)):
    return CommentService(db)

@router.get("/", response_model=List[CommentResponse])
def get_comments(post_id: int, service: CommentService = Depends(get_comment_service)):
    try:
        comments = service.get_comments_by_post(post_id)
        return comments
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=CommentResponse)
def create_comment(post_id: int, comment: CommentCreate, service: CommentService = Depends(get_comment_service)):
    try:
        new_comment = service.create_comment(post_id, comment)
        return new_comment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
