from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import post_hashtag_service
from app.core.db import get_db
from app.schemas.post_hashtag_schema import PostHashtagCreate, PostHashtagResponse
from typing import List

router = APIRouter(prefix="/post-hashtags", tags=["Post-Hashtags"])

@router.post("/link", response_model=PostHashtagResponse)
def link_post_hashtag(data: PostHashtagCreate, db: Session = Depends(get_db)):
    return post_hashtag_service.link_post_hashtag(data, db)

@router.delete("/unlink/{post_id}/{hashtag_id}")
def unlink_post_hashtag(post_id: int, hashtag_id: int, db: Session = Depends(get_db)):
    return post_hashtag_service.unlink_post_hashtag(post_id, hashtag_id, db)

@router.get("/post/{post_id}", response_model=List[PostHashtagResponse])
def get_post_hashtags(post_id: int, db: Session = Depends(get_db)):
    return post_hashtag_service.get_post_hashtags(post_id, db)

@router.get("/hashtag/{hashtag_id}", response_model=List[PostHashtagResponse])
def get_hashtag_posts(hashtag_id: int, db: Session = Depends(get_db)):
    return post_hashtag_service.get_hashtag_posts(hashtag_id, db)
