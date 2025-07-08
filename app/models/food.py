from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class FoodCategory(str, Enum):
    VEGETABLES = "vegetables"
    FRUITS = "fruits"
    GRAINS = "grains"
    PROTEINS = "proteins"
    DAIRY = "dairy"
    BEVERAGES = "beverages"
    CONDIMENTS = "condiments"

class FodmapLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    category = Column(SQLAlchemyEnum(FoodCategory), nullable=False)
    description = Column(String, nullable=True)
    
    # FODMAP content levels with UNKNOWN as default
    fructose = Column(SQLAlchemyEnum(FodmapLevel), default=FodmapLevel.UNKNOWN, nullable=False)
    lactose = Column(SQLAlchemyEnum(FodmapLevel), default=FodmapLevel.UNKNOWN, nullable=False)
    polyols = Column(SQLAlchemyEnum(FodmapLevel), default=FodmapLevel.UNKNOWN, nullable=False)
    mannitol = Column(SQLAlchemyEnum(FodmapLevel), default=FodmapLevel.UNKNOWN, nullable=False)
    sorbitol = Column(SQLAlchemyEnum(FodmapLevel), default=FodmapLevel.UNKNOWN, nullable=False)
    
    # Serving information
    serving_size = Column(String(50), nullable=True)
    serving_unit = Column(String(20), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 