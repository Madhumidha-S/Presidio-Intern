from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import comment_service
from app.services.comment_analyzer import CommentAnalyzer
from app.core.db import get_db
from app.schemas.comment_schema import CommentCreate, CommentResponse
from typing import List

router = APIRouter(prefix="/comments", tags=["Comments"])
comment_analyzer = CommentAnalyzer()

@router.get("/post/{post_id}", response_model=List[CommentResponse])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return comment_service.get_comments_by_post(post_id, db)

@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return comment_service.create_comment(comment, db)

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return comment_service.delete_comment(comment_id, db)







@router.get("/post/{post_id}/thread")
def get_comment_thread(post_id: int, db: Session = Depends(get_db)):
    return comment_analyzer.get_comment_tree(post_id, db)

@router.get("/post/{post_id}/engagement")
def get_engagement(post_id: int, db: Session = Depends(get_db)):
    tree = comment_analyzer.get_comment_tree(post_id, db)
    return {
        "engagement_depth": comment_analyzer.calculate_engagement_depth(tree),
        "total_replies": comment_analyzer.count_total_replies(tree),
    }

@router.get("/post/{post_id}/viral")
def get_viral_chains(post_id: int, min_length: int = 3, db: Session = Depends(get_db)):
    tree = comment_analyzer.get_comment_tree(post_id, db)
    return comment_analyzer.find_viral_chains(tree, min_length=min_length)

@router.get("/post/{post_id}/score")
def get_score(post_id: int, db: Session = Depends(get_db)):
    return comment_analyzer.engagement_score(post_id, db)
