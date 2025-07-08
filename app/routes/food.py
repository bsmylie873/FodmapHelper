from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db.database import get_db
from ..models.food import Food as FoodModel, FoodCategory, FodmapLevel
from ..schemas.food import Food, FoodCreate, FoodUpdate, FoodSearch
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/foods",
    tags=["foods"]
)

# List and Create endpoints (no parameters)
@router.get("/", response_model=List[Food])
def list_foods(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category: Optional[FoodCategory] = None
):
    """List food items with optional filtering."""
    try:
        query = db.query(FoodModel)
        if category:
            query = query.filter(FoodModel.category == category)
        
        # Log the query and results
        foods = query.offset(skip).limit(limit).all()
        logger.info(f"Found {len(foods)} foods in database")
        for food in foods:
            logger.info(f"Food: id={food.id}, name={food.name}")
        
        return foods
    except Exception as e:
        logger.error(f"Error listing foods: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=Food)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    """Create a new food item."""
    try:
        db_food = FoodModel(**food.dict())  # Changed from model_dump() to dict()
        db.add(db_food)
        db.commit()
        db.refresh(db_food)
        logger.info(f"Created new food: id={db_food.id}, name={db_food.name}")
        return db_food
    except Exception as e:
        logger.error(f"Error creating food: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Search endpoint (specific path)
@router.get("/search", response_model=List[Food])
def search_foods(
    query: Optional[str] = None,
    category: Optional[FoodCategory] = None,
    fodmap_type: Optional[str] = Query(None, pattern="^(fructose|lactose|polyols|mannitol|sorbitol)$"),
    fodmap_level: Optional[FodmapLevel] = None,
    db: Session = Depends(get_db)
):
    """Search food items with various filters."""
    search_query = db.query(FoodModel)

    if query:
        search_query = search_query.filter(FoodModel.name.ilike(f"%{query}%"))
    
    if category:
        search_query = search_query.filter(FoodModel.category == category)
    
    if fodmap_type and fodmap_level:
        # Dynamically filter by FODMAP type and level
        if hasattr(FoodModel, fodmap_type):
            search_query = search_query.filter(getattr(FoodModel, fodmap_type) == fodmap_level)
    
    try:
        results = search_query.all()
        logger.info(f"Search found {len(results)} results for query='{query}', category={category}, fodmap_type={fodmap_type}, fodmap_level={fodmap_level}")
        return results
    except Exception as e:
        logger.error(f"Error during food search: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# ID-based endpoints
@router.get("/{food_id}", response_model=Food)
def get_food(food_id: int, db: Session = Depends(get_db)):
    """Get a specific food item by ID."""
    logger.info(f"Attempting to fetch food with id={food_id}")
    food = db.query(FoodModel).filter(FoodModel.id == food_id).first()
    if food is None:
        logger.warning(f"Food with id={food_id} not found")
        raise HTTPException(status_code=404, detail="Food not found")
    logger.info(f"Found food: id={food.id}, name={food.name}")
    return food

@router.put("/{food_id}", response_model=Food)
def update_food(food_id: int, food: FoodUpdate, db: Session = Depends(get_db)):
    """Update a food item."""
    logger.info(f"Attempting to update food with id={food_id}")
    
    # First try to find the food
    db_food = db.query(FoodModel).filter(FoodModel.id == food_id).first()
    if db_food is None:
        logger.warning(f"Food with id={food_id} not found")
        raise HTTPException(status_code=404, detail="Food not found")
    
    try:
        # Get only the set fields from the request
        food_data = food.dict(exclude_unset=True)
        logger.info(f"Updating food {db_food.name} with data: {food_data}")
        
        # Update the food item with the new data
        for key, value in food_data.items():
            setattr(db_food, key, value)
        
        db.commit()
        db.refresh(db_food)
        logger.info(f"Successfully updated food: id={db_food.id}, name={db_food.name}")
        return db_food
    except Exception as e:
        logger.error(f"Error updating food: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{food_id}")
def delete_food(food_id: int, db: Session = Depends(get_db)):
    """Delete a food item."""
    logger.info(f"Attempting to delete food with id={food_id}")
    # First try to find the food
    food = db.query(FoodModel).filter(FoodModel.id == food_id).first()
    if food is None:
        logger.warning(f"Food with id={food_id} not found")
        raise HTTPException(status_code=404, detail="Food not found")
    
    try:
        # Log food details before deletion
        logger.info(f"Deleting food: id={food.id}, name={food.name}")
        db.delete(food)
        db.commit()
        logger.info(f"Successfully deleted food with id={food_id}")
    except Exception as e:
        logger.error(f"Error deleting food: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Food deleted successfully"} 