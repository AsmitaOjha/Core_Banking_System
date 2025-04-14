from sqlalchemy.orm import Session
from fastapi import HTTPException
from transaction.transaction_schema import TransactionCreate, Transaction
from account.account_schema import Account
from decimal import Decimal

def create_transaction(db: Session, transaction_data: TransactionCreate):
    # Step 1: Fetch sender account
    sender = db.query(Account).filter(
        Account.account_number == transaction_data.sender_account_id
    ).first()

    if not sender:
        raise HTTPException(status_code=404, detail="Sender account not found.")

    amount = Decimal(transaction_data.amount)

    # Step 2: Handle transaction types
    if transaction_data.transaction_type == "deposit":
        sender.account_balance += amount

    elif transaction_data.transaction_type == "withdraw":
        if sender.account_balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance.")
        sender.account_balance -= amount

    elif transaction_data.transaction_type in ["transfer", "payment"]:
        if sender.account_balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance.")
        sender.account_balance -= amount

        receiver = db.query(Account).filter(
            Account.account_number == transaction_data.receiver_account_id
        ).first()

        if not receiver:
            raise HTTPException(status_code=404, detail="Receiver account not found.")

        receiver.account_balance += amount
        db.add(receiver)

    # Step 3: Create transaction record
    transaction = Transaction(
        transaction_type=transaction_data.transaction_type,
        amount=amount,
        remark=transaction_data.remark,
        status=transaction_data.status,
        sender_account_id=transaction_data.sender_account_id,
        receiver_account_id=transaction_data.receiver_account_id
    )

    db.add(sender)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction
