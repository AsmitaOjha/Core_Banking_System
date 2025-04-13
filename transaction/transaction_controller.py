from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from transaction.transaction_schema import TransactionCreate, TransactionOut
from transaction.transaction_service import create_transaction
from database import get_db

transaction_router = APIRouter(prefix="/transaction", tags=["Transactions"])

@transaction_router.post("/create", response_model=TransactionOut)
def create_transaction_endpoint(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, transaction_data)
