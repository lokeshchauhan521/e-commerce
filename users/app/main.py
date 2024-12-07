from fastapi import Depends, FastAPI
from schemas import user as UserSchema
from models import user as UserModel
from core.config.db import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

UserModel.User.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

@app.get('/')
def index():    
    return {
        'message': 'Welcome to the Fastapi Users'
    }

@app.post('/users')
def create_user(request: UserSchema.User, db: Session = Depends(get_db) ):    
    new_user = UserModel.User(email = request.email, name = request.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    # return {
    #     "message": "User created successfully",
    #     "data": request
    # }

@app.get('/users')
def get_users(db: Session = Depends(get_db) ):    
    return db.query(UserModel.User).all()

@app.get('/users/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db) ):    
    return db.query(UserModel.User).filter(UserModel.User.id==user_id).first()
    