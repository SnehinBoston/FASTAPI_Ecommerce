from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from typing import List

from .database import Base

class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key= True)
    name = Column(String, unique = True)
    description = Column(String, unique= True)
    # category = 
    price = Column(Integer)
    # sku
    

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key= True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    ordered_items = relationship("Cart", back_populates="customer")

class Cart(Base):
    __tablename__ = "Cart"

    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    product_ids = list[Column(Integer, ForeignKey("Products.id"))]
    # product_name = Column(String, ForeignKey("Products.name"))
    qty = Column(Integer, default= 0)
    amount = Column(Integer, default = 0)

    customer = relationship("Users", back_populates="ordered_items")
    products = relationship("Products")
    