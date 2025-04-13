from sqlalchemy.orm import Session
from datetime import datetime
from account.account_schema import AccountCreate, Account
from user.user_schema import User  # Make sure this import exists
from fastapi import HTTPException
from decimal import Decimal

def generate_account_number(db: Session) -> str:
    last_account = db.query(Account).order_by(Account.account_number.desc()).first()

    if last_account:
        last_number = int(last_account.account_number)
        new_number = last_number + 1
    else:
        new_number = 4132025208200000

    return str(new_number)


def create_account(db: Session, account_data: AccountCreate):
    # ✅ Step 1: Check if user exists
    user = db.query(User).filter(User.id == account_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist. Please register or login first.")

    # ✅ Step 2: Generate unique account number
    account_number = generate_account_number(db)

    # ✅ Step 3: Create new account
    new_account = Account(
        account_number=account_number,
        account_type=account_data.account_type,
        account_status=account_data.account_status,
        account_balance=Decimal(account_data.account_balance),
        created_at=datetime.now(),
        closed_at=None,
        user_id=account_data.user_id,
        transaction_id=None  # Assuming optional for now
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account
