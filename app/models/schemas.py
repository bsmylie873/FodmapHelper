from pydantic import BaseModel
from typing import Optional
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