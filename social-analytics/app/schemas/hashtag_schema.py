from pydantic import BaseModel

class HashtagBase(BaseModel):
    tag: str

class HashtagCreate(HashtagBase):
    pass

class HashtagResponse(HashtagBase):
    id: int
    count: int

    class Config:
        orm_mode = True
