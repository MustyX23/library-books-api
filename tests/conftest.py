import pytest
from fastapi.testclient import TestClient

from app import storage
from app.main import app


@pytest.fixture
def client():
    storage.reset()
    return TestClient(app)
