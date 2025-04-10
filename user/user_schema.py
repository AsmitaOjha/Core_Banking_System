from sqlalchemy import Column, BigInteger, String, DateTime, Text
from sqlalchemy.orm import relationship
from database import MySQLConnection

class User(MySQLConnection.Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)    
    phone_number = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)  
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    accounts = relationship("Account", back_populates='user')

    