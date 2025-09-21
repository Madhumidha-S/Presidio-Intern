from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String(100), unique=True, nullable=False, index=True)
    count = Column(Integer, default=0)
