import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL =", DATABASE_URL)

engine = create_engine(DATABASE_URL)

print("engine=", engine)

session_local = sessionmaker(autocommit= False, autoflush=False,bind=engine)


Base= declarative_base()
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()