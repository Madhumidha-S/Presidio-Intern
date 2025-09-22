from pydantic import BaseModel

class PostHashtagBase(BaseModel):
    post_id: int
    hashtag_id: int

class PostHashtagCreate(PostHashtagBase):
    pass

class PostHashtagResponse(PostHashtagBase):
    class Config:
        orm_mode = True
