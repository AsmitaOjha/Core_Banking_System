from sqlalchemy.orm import Session
from fastapi import HTTPException
from transaction.transaction_schema import TransactionCreate, Transaction
from account.account_schema import Account
from decimal import Decimal

def create_transaction(db: Session, transaction_data: TransactionCreate):
    # Check if account exists
    account = db.query(Account).filter(Account.account_number == transaction_data.account_number).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found.")

    amount = Decimal(transaction_data.amount)

    # Handle business logic
    if transaction_data.transaction_type == "Withdrawal" and account.account_balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance.")

    # Update account balance
    if transaction_data.transaction_type == "Deposit":
        account.account_balance += amount
    elif transaction_data.transaction_type == "Withdrawal":
        account.account_balance -= amount
    elif transaction_data.transaction_type == "Transfer":
        # You can add logic here to debit from one and credit to another
        pass
    elif transaction_data.transaction_type == "Payment":
        account.account_balance -= amount

    # Create transaction record
    transaction = Transaction(
        transaction_type=transaction_data.transaction_type,
        amount=amount,
        description=transaction_data.description,
        account_number=transaction_data.account_number
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction
