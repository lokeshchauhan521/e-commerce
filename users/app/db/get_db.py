from sqlalchemy.orm import Session
from ..core.config.db import SessionLocal ,engine
from ..models.user import User as UserModel
from ..core.config.db import Base

Base.metadata.create_all(bind=engine)
print("Registered tables:", Base.metadata.tables.keys())
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
