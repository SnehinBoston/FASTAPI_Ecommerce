from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/", response_model = schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db = db, user= user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, limit=limit)
    return users

@app.post("/users/{user_id}/cart/", response_model=schemas.Cart)
def create_cart_for_user(user_id: int, cart: schemas.CartCreate, product_ids = List[int], db: Session = Depends(get_db)):
    return crud.create_cart(db=db, cart=cart, user_id=user_id, product_ids = product_ids)

@app.get("/users/{user_id}/cart", response_model=schemas.Cart)
def get_cart_for_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_cart_by_user_id(db = db, user_id=user_id)
