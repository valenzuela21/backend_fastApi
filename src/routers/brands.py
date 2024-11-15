from typing import List
from src.utils.dbUtil import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import Brand
from src.schemas.brandsChema import BrandCreate, BrandOut
from src.repository.crudRepository import get_item_by_name, create_item, get_all_items, get_item_by_id, update_item, \
    delete_item

from src.utils.jwtUtil import JWTBearer

router = APIRouter(
    prefix="/brands",
    tags=["Brands"],
    dependencies=[Depends(get_db),  Depends(JWTBearer())]
)

@router.post("/create", response_model=BrandCreate)
def create_category(brand: BrandCreate, db: Session = Depends(get_db)):
    existing_category = get_item_by_name(db, Brand, brand.name)
    if existing_category:
        raise HTTPException(status_code=400, detail="Brand already exists")

    new_category = create_item(db, Brand, brand.name)
    return new_category

@router.get("/all", response_model=List[BrandOut])
def list_categories(db: Session = Depends(get_db)):
    categories = get_all_items(db, Brand)
    return categories

@router.put("/update/{brand_id}", response_model=BrandOut)
def update_category(brand_id: int, brand: BrandCreate, db: Session = Depends(get_db)):
    db_brand = get_item_by_id(db, Brand, brand_id)
    if not db_brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    updated_brand = update_item(db, Brand, brand_id, brand.name)
    return updated_brand

@router.delete("/delete/{brand_id}", response_model=BrandOut)
def delete_category(brand_id: int, db: Session = Depends(get_db)):
    db_brand = get_item_by_id(db, Brand, brand_id)
    if not db_brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    delete_item(db, Brand, brand_id)
    return {"message": "Brand deleted successfully"}