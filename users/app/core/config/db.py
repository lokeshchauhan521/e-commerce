from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .environment import POSTGRES_DB_URL


engine = create_engine(POSTGRES_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# print("Registered tables:", Base.metadata.tables.keys())
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
