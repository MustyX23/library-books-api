import pytest
from fastapi.testclient import TestClient

from app import storage
from app.main import app


@pytest.fixture
def client():
    storage.reset()
    return TestClient(app)


@pytest.fixture
def book(client):
    return client.post("/books", json={"title": "1984", "author": "George Orwell", "year": 1949}).json()
