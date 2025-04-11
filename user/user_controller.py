from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from user.user_schema import UserCreate, UserOut
from user.user_service import create_user
from database import MySQLConnection

user_router = APIRouter()

def get_db():
    db = MySQLConnection.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post("/register", response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(user_data, db)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
