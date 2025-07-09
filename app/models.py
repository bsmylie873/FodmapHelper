from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base
import enum

class FodmapLevel(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    
    # Relationship with foods
    foods = relationship("Food", back_populates="category")

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fodmap_level = Column(Enum(FodmapLevel))
    serving_size = Column(String)
    description = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    
    # Foreign key to category
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="foods") 