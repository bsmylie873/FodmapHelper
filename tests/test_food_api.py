import pytest
from app.models.food import FoodCategory, FodmapLevel

def test_create_food(client):
    """Test creating a new food item."""
    food_data = {
        "name": "Test Apple",
        "category": "fruits",
        "description": "Test apple description",
        "fructose": "high",
        "lactose": "low",
        "polyols": "low",
        "mannitol": "low",
        "sorbitol": "high",
        "serving_size": "1",
        "serving_unit": "medium"
    }
    
    response = client.post("/foods/", json=food_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == food_data["name"]
    assert data["category"] == food_data["category"]
    assert "id" in data
    assert data["fructose"] == food_data["fructose"]

def test_get_food(client, sample_foods):
    """Test getting a specific food item."""
    # Get the first sample food
    food = sample_foods[0]
    response = client.get(f"/foods/{food.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == food.name
    assert data["category"] == food.category.value

def test_get_nonexistent_food(client):
    """Test getting a food item that doesn't exist."""
    response = client.get("/foods/9999")
    assert response.status_code == 404

def test_list_foods(client, sample_foods):
    """Test listing all food items."""
    response = client.get("/foods/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(sample_foods)
    assert data[0]["name"] == sample_foods[0].name

def test_search_foods(client, sample_foods):
    """Test searching food items."""
    # Test search by name
    response = client.get("/foods/search?query=Garlic")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Test Garlic"

    # Test search by category
    response = client.get("/foods/search?category=vegetables")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["category"] == "vegetables"

    # Test search by FODMAP content
    response = client.get("/foods/search?fodmap_type=fructose&fodmap_level=high")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["fructose"] == "high"

def test_update_food(client, sample_foods):
    """Test updating a food item."""
    food = sample_foods[0]
    update_data = {
        "name": "Updated Test Garlic",
        "description": "Updated description"
    }
    
    response = client.put(f"/foods/{food.id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["description"] == update_data["description"]
    # Check that unmodified fields remain unchanged
    assert data["category"] == food.category.value
    assert data["fructose"] == food.fructose.value

def test_update_nonexistent_food(client):
    """Test updating a food item that doesn't exist."""
    update_data = {"name": "Test Food"}
    response = client.put("/foods/9999", json=update_data)
    assert response.status_code == 404

def test_delete_food(client, sample_foods):
    """Test deleting a food item."""
    food = sample_foods[0]
    response = client.delete(f"/foods/{food.id}")
    assert response.status_code == 200
    
    # Verify the food is deleted
    response = client.get(f"/foods/{food.id}")
    assert response.status_code == 404

def test_delete_nonexistent_food(client):
    """Test deleting a food item that doesn't exist."""
    response = client.delete("/foods/9999")
    assert response.status_code == 404 