from fastapi import APIRouter

router = APIRouter()

@router.get("/products/<int:product_id>", tags=["products"])
def get_products():
    return 

@router.post("/products/", tags=["products"])
def post_products():
    return 
