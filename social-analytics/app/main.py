from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import hashtag_router
from app.core.db import Base, engine

app = FastAPI(title="Social Media Analytics API")
app.include_router(hashtag_router.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"msg": "Social Media Analytics API"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse({"detail": "Internal server error"}, status_code=500)