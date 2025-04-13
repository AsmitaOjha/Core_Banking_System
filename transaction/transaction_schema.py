from sqlalchemy import Column, BigInteger, DateTime, Enum, ForeignKey, DECIMAL, String, func
from sqlalchemy.orm import relationship
from database import MySQLConnection
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

class Transaction(MySQLConnection.Base):
    __tablename__ = "transactions"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    transaction_type = Column(Enum("Deposit", "Withdrawal", "Transfer", "Payment"), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    transaction_time = Column(DateTime, nullable=False, default=func.now())
    description = Column(String(255), nullable=True)
    
    # Foreign key to account
    account_number = Column(String(20), ForeignKey('accounts.account_number', ondelete='CASCADE'), nullable=False)

    # Relationship to Account
    accounts = relationship("Account", back_populates="transactions")


# Pydantic Input Model
class TransactionCreate(BaseModel):
    transaction_type: Literal["Deposit", "Withdrawal", "Transfer", "Payment"]
    amount: float
    description: Optional[str]
    account_number: str


# Pydantic Output Model
class TransactionOut(BaseModel):
    id: int
    transaction_type: str
    amount: float
    transaction_time: datetime
    description: Optional[str]
    account_number: str

    class Config:
        from_attributes = True
