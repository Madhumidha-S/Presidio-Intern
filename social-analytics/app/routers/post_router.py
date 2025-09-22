from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import post_service
from app.core.db import get_db
from app.schemas.post_schema import PostCreate, PostResponse
from typing import List

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return post_service.get_posts(db)

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(post, db)

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.get_post(post_id, db)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.delete_post(post_id, db)
