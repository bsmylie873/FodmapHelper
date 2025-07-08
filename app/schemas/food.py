from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..models.food import FodmapLevel, FoodCategory


class FoodBase(BaseModel):
    """Base schema for food items."""
    name: str = Field(..., min_length=1, max_length=100)
    category: FoodCategory
    description: Optional[str] = None
    fructose: FodmapLevel = FodmapLevel.UNKNOWN
    lactose: FodmapLevel = FodmapLevel.UNKNOWN
    polyols: FodmapLevel = FodmapLevel.UNKNOWN
    mannitol: FodmapLevel = FodmapLevel.UNKNOWN
    sorbitol: FodmapLevel = FodmapLevel.UNKNOWN
    serving_size: Optional[str] = None
    serving_unit: Optional[str] = None


class FoodCreate(FoodBase):
    """Schema for creating food items."""
    pass


class Food(FoodBase):
    """Schema for food items with database fields."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True  # This is the correct setting for Pydantic v1
        json_encoders = {
            datetime: lambda dt: dt.isoformat() if dt else None
        }


class FoodUpdate(BaseModel):
    """Schema for updating food items."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    category: Optional[FoodCategory] = None
    description: Optional[str] = None
    fructose: Optional[FodmapLevel] = None
    lactose: Optional[FodmapLevel] = None
    polyols: Optional[FodmapLevel] = None
    mannitol: Optional[FodmapLevel] = None
    sorbitol: Optional[FodmapLevel] = None
    serving_size: Optional[str] = None
    serving_unit: Optional[str] = None


class FoodSearch(BaseModel):
    """Schema for food search parameters."""
    query: Optional[str] = None
    category: Optional[FoodCategory] = None
    fodmap_type: Optional[str] = Field(None, pattern="^(fructose|lactose|polyols|mannitol|sorbitol)$")
    fodmap_level: Optional[FodmapLevel] = None 