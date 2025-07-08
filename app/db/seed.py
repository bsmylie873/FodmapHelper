from sqlalchemy.orm import Session
from app.models.food import Food, FoodCategory, FodmapLevel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_default_fodmap_levels():
    """Get default FODMAP levels dictionary."""
    return {
        "fructose": FodmapLevel.UNKNOWN,
        "lactose": FodmapLevel.UNKNOWN,
        "polyols": FodmapLevel.UNKNOWN,
        "mannitol": FodmapLevel.UNKNOWN,
        "sorbitol": FodmapLevel.UNKNOWN
    }

sample_foods = [
    # Vegetables
    {
        "id": 1,
        "name": "Spinach",
        "category": FoodCategory.VEGETABLES,
        "description": "Fresh spinach leaves",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "cup raw"
    },
    {
        "id": 2,
        "name": "Carrot",
        "category": FoodCategory.VEGETABLES,
        "description": "Fresh carrots",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "medium carrot"
    },
    {
        "id": 3,
        "name": "Garlic",
        "category": FoodCategory.VEGETABLES,
        "description": "Fresh garlic cloves",
        "fructose": FodmapLevel.HIGH,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "clove"
    },
    {
        "id": 4,
        "name": "Bell Pepper",
        "category": FoodCategory.VEGETABLES,
        "description": "Fresh bell pepper",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "medium pepper"
    },
    {
        "id": 5,
        "name": "Onion",
        "category": FoodCategory.VEGETABLES,
        "description": "Fresh onion",
        "fructose": FodmapLevel.HIGH,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "medium onion"
    },
    # Fruits
    {
        "id": 6,
        "name": "Apple",
        "category": FoodCategory.FRUITS,
        "description": "Fresh apple with skin",
        "fructose": FodmapLevel.HIGH,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.HIGH,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.HIGH,
        "serving_size": "1",
        "serving_unit": "medium apple"
    },
    {
        "id": 7,
        "name": "Banana",
        "category": FoodCategory.FRUITS,
        "description": "Ripe banana",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "medium banana"
    },
    {
        "id": 8,
        "name": "Orange",
        "category": FoodCategory.FRUITS,
        "description": "Fresh orange",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "medium orange"
    },
    # Dairy
    {
        "id": 9,
        "name": "Milk",
        "category": FoodCategory.DAIRY,
        "description": "Regular cow's milk",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.HIGH,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "cup"
    },
    {
        "id": 10,
        "name": "Hard Cheese",
        "category": FoodCategory.DAIRY,
        "description": "Aged cheddar cheese",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "40",
        "serving_unit": "grams"
    },
    # Grains
    {
        "id": 11,
        "name": "Wheat Bread",
        "category": FoodCategory.GRAINS,
        "description": "Regular wheat bread",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "slice"
    },
    {
        "id": 12,
        "name": "Quinoa",
        "category": FoodCategory.GRAINS,
        "description": "Cooked quinoa",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "cup cooked"
    },
    # Proteins
    {
        "id": 13,
        "name": "Chicken Breast",
        "category": FoodCategory.PROTEINS,
        "description": "Plain chicken breast",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "100",
        "serving_unit": "grams"
    },
    {
        "id": 14,
        "name": "Tofu",
        "category": FoodCategory.PROTEINS,
        "description": "Firm tofu",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "100",
        "serving_unit": "grams"
    },
    # Beverages
    {
        "id": 15,
        "name": "Green Tea",
        "category": FoodCategory.BEVERAGES,
        "description": "Brewed green tea",
        "fructose": FodmapLevel.LOW,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "cup"
    },
    # Condiments
    {
        "id": 16,
        "name": "Honey",
        "category": FoodCategory.CONDIMENTS,
        "description": "Pure honey",
        "fructose": FodmapLevel.HIGH,
        "lactose": FodmapLevel.LOW,
        "polyols": FodmapLevel.LOW,
        "mannitol": FodmapLevel.LOW,
        "sorbitol": FodmapLevel.LOW,
        "serving_size": "1",
        "serving_unit": "tablespoon"
    }
]

def seed_database(db: Session, force_reset: bool = False):
    """Seed the database with sample food data.
    
    Args:
        db: Database session
        force_reset: If True, will clear existing data before seeding
    """
    # Check if database is already seeded
    existing_count = db.query(Food).count()
    logger.info(f"Found {existing_count} existing food items in database")
    
    if existing_count > 0:
        if not force_reset:
            logger.info("Database already contains data. Use force_reset=True to reseed.")
            return
        else:
            logger.info("Clearing existing data...")
            db.query(Food).delete()
            db.commit()
            logger.info("Existing data cleared successfully")
    
    logger.info("Starting database seeding...")
    for food_data in sample_foods:
        food = Food(**food_data)
        db.add(food)
        logger.debug(f"Added food: {food.name} (ID: {food.id})")
    
    try:
        db.commit()
        final_count = db.query(Food).count()
        logger.info(f"Database seeding completed. Added {final_count} food items.")
    except Exception as e:
        logger.error(f"Error during database seeding: {str(e)}")
        db.rollback()
        raise 