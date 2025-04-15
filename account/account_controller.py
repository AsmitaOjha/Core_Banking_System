from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from account.account_schema import AccountCreate, AccountOut
from account.account_service import create_account
from account.account_service import create_account, view_account


account_router = APIRouter()

@account_router.post("/create", response_model=AccountOut)
def account_creation(account_data: AccountCreate, db: Session = Depends(get_db)):
    try:
        new_account = create_account(db, account_data)
        return new_account
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@account_router.get("/view/{account_number}", response_model=AccountOut)
def get_account(account_number: str, db: Session = Depends(get_db)):
    try:
        account = view_account(db, account_number)
        return account
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

