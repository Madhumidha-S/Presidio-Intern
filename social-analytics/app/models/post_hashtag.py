from sqlalchemy import Column, Integer, ForeignKey, Table
from app.core.db import Base

class PostHashtag(Base):
    __tablename__ = "post_hashtags"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    hashtag_id = Column(Integer, ForeignKey("hashtags.id", ondelete="CASCADE"), primary_key=True)
