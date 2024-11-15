from fastapi import APIRouter, Depends, HTTPException, status, Response
from src.schemas.categoryChema import CategoryCreate
from sqlalchemy.orm import Session
from typing import List
from src.models import Category
from src.repository.crudRepository import create_item, get_item_by_name, get_item_by_id, get_all_items, update_item, delete_item
from src.schemas.sharedChema import CategoryOut

from src.utils.dbUtil import get_db
from src.utils.jwtUtil import JWTBearer

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    dependencies=[ Depends(get_db),  Depends(JWTBearer()) ]
)

@router.post("/create", response_model=CategoryCreate, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    existing_category = get_item_by_name(db, Category, category.name)
    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    new_category = create_item(db, Category, category.name)
    return new_category

@router.get("/all", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    categories = get_all_items(db, Category)
    return categories

@router.put("/update/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = get_item_by_id(db, Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    updated_category = update_item(db, Category, category_id, category.name)
    return updated_category

@router.delete("/delete/{category_id}", response_model=CategoryOut)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_item_by_id(db, Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    delete_item(db, Category, category_id)
    return {"message": "Category deleted successfully"}