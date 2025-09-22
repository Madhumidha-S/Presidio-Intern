from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import hashtag_service, hashtag_engine
from app.core.db import get_db
from app.schemas.hashtag_schema import HashtagCreate, HashtagResponse
from typing import List

router = APIRouter(prefix="/hashtags", tags=["Hashtags"])

@router.get("/", response_model=List[HashtagResponse])
def get_hashtags(db: Session = Depends(get_db)):
    return hashtag_service.get_hashtags(db)

@router.post("/", response_model=HashtagResponse)
def create_hashtag(hashtag: HashtagCreate, db: Session = Depends(get_db)):
    return hashtag_service.create_hashtag(hashtag, db)

@router.delete("/{hashtag_id}")
def delete_hashtag(hashtag_id: int, db: Session = Depends(get_db)):
    return hashtag_service.delete_hashtag(hashtag_id, db)

@router.get("/trending")
def trending(limit: int = 10):
    return hashtag_engine.get_trending(limit)

@router.get("/recommend/{tag}")
def recommend(tag: str, db: Session = Depends(get_db), min_rate: float = 0.3, top_n: int = 3):
    return hashtag_engine.recommend(tag, db=db, min_cooccurrence=min_rate, top_n=top_n)
