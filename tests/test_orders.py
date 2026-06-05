import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_docs():
    """Test que la documentación está disponible"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_create_order():
    """Test crear una orden"""
    response = client.post("/orders/", json={"customer_name": "Test User", "total_amount": 100.0})
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["customer_name"] == "Test User"
    assert data["total_amount"] == 100.0


def test_health_check():
    """Test health check endpoint si existe"""
    response = client.get("/")
    # Ajusta según tu endpoint root
    assert response.status_code in [200, 404]
