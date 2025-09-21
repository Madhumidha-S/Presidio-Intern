from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from app.core.db import Base

class PostHashtag(Base):
    __tablename__ = "post_hashtags"
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    hashtag_id = Column(Integer, ForeignKey("hashtags.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('post_id', 'hashtag_id', name='pk_post_hashtag'),)
