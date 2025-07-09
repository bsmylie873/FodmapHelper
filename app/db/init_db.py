from sqlalchemy.orm import Session
from app.models.food import Food, Category, FodmapLevel

def init_db(db: Session, force_reset: bool = False):
    """Initialize the database with default data."""
    if force_reset:
        # Drop all existing data
        db.query(Food).delete()
        db.query(Category).delete()
        db.commit()

    # Create default categories if they don't exist
    default_categories = [
        {"name": "Vegetables", "description": "Fresh and cooked vegetables"},
        {"name": "Fruits", "description": "Fresh and dried fruits"},
        {"name": "Grains", "description": "Breads, cereals, and grains"},
        {"name": "Proteins", "description": "Meat, fish, and plant-based proteins"},
        {"name": "Dairy", "description": "Milk, cheese, and dairy products"},
        {"name": "Beverages", "description": "Drinks and liquid foods"},
        {"name": "Condiments", "description": "Sauces, spreads, and seasonings"}
    ]

    for cat_data in default_categories:
        if not db.query(Category).filter(Category.name == cat_data["name"]).first():
            category = Category(**cat_data)
            db.add(category)
    
    db.commit()

    # Get categories for reference
    vegetables = db.query(Category).filter(Category.name == "Vegetables").first()
    fruits = db.query(Category).filter(Category.name == "Fruits").first()
    grains = db.query(Category).filter(Category.name == "Grains").first()
    proteins = db.query(Category).filter(Category.name == "Proteins").first()
    dairy = db.query(Category).filter(Category.name == "Dairy").first()

    # Add some example foods if they don't exist
    example_foods = [
        {
            "name": "Garlic",
            "category_id": vegetables.id,
            "fodmap_level": FodmapLevel.HIGH,
            "serving_size": "1 clove",
            "description": "Common cooking ingredient",
            "notes": "High in fructans"
        },
        {
            "name": "Banana",
            "category_id": fruits.id,
            "fodmap_level": FodmapLevel.LOW,
            "serving_size": "1 medium",
            "description": "Ripe banana",
            "notes": "Ripe bananas are generally well tolerated"
        },
        {
            "name": "Sourdough Bread",
            "category_id": grains.id,
            "fodmap_level": FodmapLevel.LOW,
            "serving_size": "2 slices",
            "description": "Traditional sourdough bread",
            "notes": "The fermentation process reduces FODMAP content"
        },
        {
            "name": "Chicken Breast",
            "category_id": proteins.id,
            "fodmap_level": FodmapLevel.LOW,
            "serving_size": "100g",
            "description": "Lean meat protein",
            "notes": "All plain meat is naturally low in FODMAPs"
        },
        {
            "name": "Milk",
            "category_id": dairy.id,
            "fodmap_level": FodmapLevel.HIGH,
            "serving_size": "250ml",
            "description": "Regular cow's milk",
            "notes": "Contains lactose"
        }
    ]

    for food_data in example_foods:
        if not db.query(Food).filter(Food.name == food_data["name"]).first():
            food = Food(**food_data)
            db.add(food)
    
    db.commit() 