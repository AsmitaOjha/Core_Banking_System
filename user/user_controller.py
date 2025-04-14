from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from user.user_schema import UserCreate, UserOut
from user.user_service import create_user, get_user_by_email


user_router = APIRouter()

@user_router.post("/register", response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(user_data, db)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/exists")
def check_user_exists(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    return {"exists": bool(user)}