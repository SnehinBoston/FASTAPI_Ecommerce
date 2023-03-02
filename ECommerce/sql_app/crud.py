from sqlalchemy.orm import Session

from . import models, schemas
from typing import List

# User table
def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id)

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, limit: int = 100):
    return db.query(models.User).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "abstract"
    db_user = models.User(name = user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Product table
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id)

def get_product_by_name(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.name == product_name)

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name = product.name, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Cart table
def create_cart(db: Session, cart: schemas.CartCreate, user_id: int, product_ids: List[int]):
    db_cart = models.Cart(**cart.dict(), user_id = user_id, product_ids = product_ids)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def get_cart_by_user_id(db: Session, user_id: int):
    return db.query(models.Cart).filter(models.Cart.user_id == user_id)