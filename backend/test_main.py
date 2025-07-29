import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
from app import models

# Test database
SQLITE_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create test database
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_movies_empty():
    response = client.get("/api/movies/")
    assert response.status_code == 200
    assert response.json() == []

def test_get_genres_empty():
    response = client.get("/api/genres/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_genre():
    genre_data = {"name": "Test Genre", "description": "A test genre"}
    response = client.post("/api/genres/", json=genre_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Genre"
    assert data["description"] == "A test genre"
    assert "id" in data

def test_create_director():
    director_data = {"name": "Test Director", "birth_year": 1980, "bio": "A test director"}
    response = client.post("/api/directors/", json=director_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Director"
    assert data["birth_year"] == 1980

def test_create_actor():
    actor_data = {"name": "Test Actor", "birth_year": 1985, "bio": "A test actor"}
    response = client.post("/api/actors/", json=actor_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Actor"
    assert data["birth_year"] == 1985

def test_movie_not_found():
    response = client.get("/api/movies/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"} 