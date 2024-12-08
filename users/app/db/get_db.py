from ..core.config.db import SessionLocal ,engine, Base

Base.metadata.create_all(bind=engine)
# print("Registered tables:", Base.metadata.tables.keys())
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
