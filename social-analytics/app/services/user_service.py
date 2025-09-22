from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

def get_users(db: Session):
    return db.query(User).all()

def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def create_user(user_data: UserCreate, db: Session):
    user = User(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": f"User with id {user_id} not found"}
    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted"}
