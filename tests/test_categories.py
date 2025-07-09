from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest
from app.main import app
from app.database import Base
from app.dependencies import get_db

# Use in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

def test_create_category(client):
    response = client.post(
        "/categories/",
        json={"name": "Fruits", "description": "Fresh and dried fruits"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Fruits"
    assert data["description"] == "Fresh and dried fruits"
    assert "id" in data
    assert data["food_count"] == 0

def test_create_duplicate_category(client):
    # Create first category
    client.post(
        "/categories/",
        json={"name": "Vegetables", "description": "Fresh vegetables"}
    )
    
    # Try to create duplicate
    response = client.post(
        "/categories/",
        json={"name": "Vegetables", "description": "Different description"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Category already exists"

def test_read_categories(client):
    # Create test categories
    categories = [
        {"name": "Fruits", "description": "Fresh fruits"},
        {"name": "Vegetables", "description": "Fresh vegetables"},
        {"name": "Grains", "description": "Whole grains"}
    ]
    for category in categories:
        client.post("/categories/", json=category)
    
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert all(item["food_count"] == 0 for item in data)

def test_read_category(client):
    # Create a category
    create_response = client.post(
        "/categories/",
        json={"name": "Fruits", "description": "Fresh fruits"}
    )
    category_id = create_response.json()["id"]
    
    # Read the category
    response = client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Fruits"
    assert data["description"] == "Fresh fruits"
    assert data["id"] == category_id

def test_read_nonexistent_category(client):
    response = client.get("/categories/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"

def test_update_category(client):
    # Create a category
    create_response = client.post(
        "/categories/",
        json={"name": "Fruits", "description": "Fresh fruits"}
    )
    category_id = create_response.json()["id"]
    
    # Update the category
    response = client.put(
        f"/categories/{category_id}",
        json={"name": "Fresh Fruits", "description": "Fresh and seasonal fruits"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Fresh Fruits"
    assert data["description"] == "Fresh and seasonal fruits"

def test_update_nonexistent_category(client):
    response = client.put(
        "/categories/999",
        json={"name": "Test", "description": "Test description"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"

def test_delete_category(client):
    # Create a category
    create_response = client.post(
        "/categories/",
        json={"name": "Fruits", "description": "Fresh fruits"}
    )
    category_id = create_response.json()["id"]
    
    # Delete the category
    response = client.delete(f"/categories/{category_id}")
    assert response.status_code == 200
    assert response.json()["ok"] == True
    
    # Verify category is deleted
    get_response = client.get(f"/categories/{category_id}")
    assert get_response.status_code == 404

def test_delete_nonexistent_category(client):
    response = client.delete("/categories/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"

def test_category_with_foods(client):
    # Create a category
    category_response = client.post(
        "/categories/",
        json={"name": "Fruits", "description": "Fresh fruits"}
    )
    category_id = category_response.json()["id"]
    
    # Create foods in the category
    foods = [
        {
            "name": "Apple",
            "fodmap_level": "low",
            "serving_size": "1 medium",
            "category_id": category_id
        },
        {
            "name": "Banana",
            "fodmap_level": "high",
            "serving_size": "1 medium",
            "category_id": category_id
        }
    ]
    for food in foods:
        client.post("/foods/", json=food)
    
    # Verify category food count
    response = client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["food_count"] == 2
    
    # Get foods by category
    foods_response = client.get(f"/foods?category_id={category_id}")
    assert foods_response.status_code == 200
    foods_data = foods_response.json()
    assert len(foods_data) == 2
    assert all(food["category_id"] == category_id for food in foods_data) 