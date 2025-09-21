from fastapi import APIRouter
from app.services import hashtag_service

router = APIRouter(prefix="/hashtags", tags=["Hashtags"])

@router.get("/trending")
def trending():
    return {"trending": hashtag_service.get_trending()}

@router.get("/recommend/{tag}")
def recommend(tag: str):
    return {"recommendations": hashtag_service.recommend(tag)}
