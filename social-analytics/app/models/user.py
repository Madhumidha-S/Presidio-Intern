from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from app.core.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # <-- added
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
