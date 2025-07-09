from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class FodmapLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    food_count: int = 0

    class Config:
        from_attributes = True

class FoodBase(BaseModel):
    name: str
    fodmap_level: FodmapLevel
    serving_size: str
    description: Optional[str] = None
    notes: Optional[str] = None

class FoodCreate(FoodBase):
    category_id: int

class Food(FoodBase):
    id: int
    category_id: int
    category: Category

    class Config:
        from_attributes = True

class FoodUpdate(BaseModel):
    name: Optional[str] = None
    fodmap_level: Optional[FodmapLevel] = None
    serving_size: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    category_id: Optional[int] = None 