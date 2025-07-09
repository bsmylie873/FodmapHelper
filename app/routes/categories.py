from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.db.crud import get_category, get_category_by_name, get_categories, create_category, update_category, delete_category
from app.models.schemas import Category, CategoryCreate, CategoryBase

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=List[Category])
def read_categories(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    db: Session = Depends(get_db)
):
    """
    Get all categories with pagination support.
    """
    categories = get_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    """
    Get a specific category by ID.
    """
    db_category = get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.post("/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """
    Create a new category.
    """
    db_category = get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return create_category(db=db, category=category)

@router.put("/{category_id}", response_model=Category)
def update_existing_category(
    category_id: int,
    category: CategoryBase,
    db: Session = Depends(get_db)
):
    """
    Update a category by ID.
    """
    db_category = update_category(db, category_id=category_id, category=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/{category_id}")
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    """
    Delete a category by ID.
    """
    success = delete_category(db, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"ok": True} 