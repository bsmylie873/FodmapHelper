import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.database import Base, get_db
from app.models.food import Food, FoodCategory, FodmapLevel

# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def test_db():
    """Create a fresh database for each test."""
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new session for the test
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after the test
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with a fresh database."""
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()
    
    # Override the database dependency
    app.dependency_overrides[get_db] = override_get_db
    
    # Disable database initialization on startup for tests
    app.router.on_startup = []
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def sample_foods(test_db):
    """Create sample food items for testing."""
    foods = [
        Food(
            name="Test Garlic",
            category=FoodCategory.VEGETABLES,
            description="Test garlic description",
            fructose=FodmapLevel.HIGH,
            lactose=FodmapLevel.LOW,
            polyols=FodmapLevel.LOW,
            mannitol=FodmapLevel.LOW,
            sorbitol=FodmapLevel.LOW,
            serving_size="1",
            serving_unit="clove"
        ),
        Food(
            name="Test Banana",
            category=FoodCategory.FRUITS,
            description="Test banana description",
            fructose=FodmapLevel.LOW,
            lactose=FodmapLevel.LOW,
            polyols=FodmapLevel.LOW,
            mannitol=FodmapLevel.LOW,
            sorbitol=FodmapLevel.LOW,
            serving_size="1",
            serving_unit="medium"
        ),
    ]
    
    for food in foods:
        test_db.add(food)
    test_db.commit()
    
    return foods 