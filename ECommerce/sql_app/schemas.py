from typing import List, Union

from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class ProductCreate(ProductBase):
    pass

class UserBase(BaseModel):
    name :str
    email :str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    is_active: bool
    hashed_password: str

class CartBase(BaseModel):
    qty : int
    amount: int

class Cart(CartBase):
    id: int
    user_id: int
    product_ids: List[int]
    class Config:
        orm_mode = True

class CartCreate(CartBase):
    pass