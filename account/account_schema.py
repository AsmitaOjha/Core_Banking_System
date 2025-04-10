from sqlalchemy import Column, BigInteger, DateTime, Enum, String, ForeignKey
from sqlalchemy.orm import relationship
from database import MySQLConnection

class Account(MySQLConnection.Base):
    __tablename__ = "accounts"

    account_number = Column(String(20),primary_key=True)
    account_type = Column(Enum("Saving", "Current","Fixed Deposit"), nullable=False, default="Saving")
    account_status = Column(Enum("Active", "Closed"), nullable=False)
    balance = Column(BigInteger, nullable=False, default=0) 
    created_at = Column(DateTime, nullable=False)   
    closed_at = Column(DateTime, nullable=True) 
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    transaction_id = Column(BigInteger, ForeignKey('transactions.id', ondelete='CASCADE'), nullable=False)

    users = relationship("User",back_populates='account')
    transactions = relationship("Transaction", back_populates='account')

