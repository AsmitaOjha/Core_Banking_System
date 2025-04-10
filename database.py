from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class MySQLConnection:
    __connection = None
    Base = declarative_base()

    @classmethod
    def get_connection(cls):
        if cls.__connection is None:
            user = os.getenv("DB_USERNAME")
            password = os.getenv("DB_PASSWORD")
            db_name = os.getenv("DB_DATABASE")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")

            if not user:
                exit("Please set the environment variable DB_USERNAME")

            DB_URL = f"mysql+pymysql://{user}:{quote_plus(password)}@{db_host}:{db_port}/{db_name}"
            engine = create_engine(DB_URL, echo=True)
            cls.Base = declarative_base()
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            cls.__connection = SessionLocal

        return cls.__connection()

