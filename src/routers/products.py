from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from src.repository.crudRepository import get_item_by_id
from src.schemas.productsChema import ProductCreate, ProductOut
from src.models import Product, Category, Brand
from src.utils.dbUtil import get_db

from src.utils.jwtUtil import JWTBearer

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    dependencies=[Depends(get_db), Depends(JWTBearer())]
)


@router.post("/create", response_model=ProductOut)
def createProduct(product: ProductCreate, db: Session = Depends(get_db)):

    db_category = get_item_by_id(db, Category, product.category_id)

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_brand = get_item_by_id(db, Brand, product.brand_id)
    if not db_brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    if product.rating > 5.0:
        raise HTTPException(status_code=401, detail="The rating is a maximum of 5")

    db_item = Product(
        name=product.name,  # Assuming 'name' is a field in both ProductCreate and Product
        description=product.description,
        price=product.price,
        category_id=product.category_id,
        brand_id=product.brand_id,
        rating=product.rating,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/list", response_model=Page[ProductOut])
async def listProducts(db: Session = Depends(get_db)):

    products_query = db.query(Product)

    return paginate(products_query)

@router.get("/{producto_id}", response_model=ProductOut)
def get_product(
    producto_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(Product.id == producto_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product
