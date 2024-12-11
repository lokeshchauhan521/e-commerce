from ..core.config.db import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine, checkfirst=True)


# print("Registered tables:", Base.metadata.tables.keys())
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
