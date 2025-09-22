from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    user_id: int
    post_id: int
    parent_id: Optional[int] = None

class CommentResponse(CommentBase):
    id: int
    user_id: int
    post_id: int
    parent_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True
