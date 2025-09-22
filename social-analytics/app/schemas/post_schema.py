from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    user_id: int

class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
