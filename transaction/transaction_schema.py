from sqlalchemy import Column, String, Enum, ForeignKey, BigInteger, TIMESTAMP, DATETIME
from sqlalchemy.orm import relationship
from database import MySQLConnection

class Transaction(MySQLConnection.Base):
    __tablename__ = 'transactions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)   
    sender_account_id = Column(BigInteger, ForeignKey('accounts.id'), nullable=False)   
    receiver_account_id = Column(BigInteger, ForeignKey('accounts.id'), nullable=True) 
    amount = Column(BigInteger, nullable=False)
    type = Column(Enum('deposit', 'withdraw', 'transfer'), nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    remark = Column(String(255), nullable=False)
    status = Column(Enum("Completed","Failed","Pending"))
    accounts = relationship("Account", back_populates="transaction")