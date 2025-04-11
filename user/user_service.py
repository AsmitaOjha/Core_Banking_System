from user.user_schema import User, UserCreate
from sqlalchemy.orm import Session

def create_user(user_data: UserCreate, db: Session):
    new_user = User(
        name= user_data.name,
        date_of_birth= user_data.date_of_birth,
        gender= user_data.gender,
        phone_number= user_data.phone_number,
        email= user_data.email,
        password= user_data.password,
        city= user_data.city,
        state= user_data.state,
        country= user_data.country
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user