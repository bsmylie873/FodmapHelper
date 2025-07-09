import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base
from app.dependencies import get_db

# Use in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    return engine

@pytest.fixture(scope="session")
def TestingSessionLocal(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db(TestingSessionLocal):
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def override_get_db(db):
    def _override_get_db():
        try:
            yield db
        finally:
            pass
    return _override_get_db

@pytest.fixture
def client(engine, override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()

@pytest.fixture
def test_category(client):
    response = client.post(
        "/categories/",
        json={"name": "Test Category", "description": "Test Description"}
    )
    return response.json()

@pytest.fixture
def test_food(client, test_category):
    response = client.post(
        "/foods/",
        json={
            "name": "Test Food",
            "fodmap_level": "low",
            "serving_size": "100g",
            "category_id": test_category["id"]
        }
    )
    return response.json() 