import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def auth_token():
    """Fixture para obtener un token de autenticación"""
    response = client.post(
        "/login",
        data={"username": "david@example.com", "password": "123456"},
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_create_order_e2e(auth_token):
    """Test E2E: Crear una orden con autenticación"""
    response = client.post(
        "/orders/",
        json={
            "customer_name": "E2E",
            "total_amount": 300,
        },
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "E2E"
    assert data["total_amount"] == 300


def test_login_success():
    """Test: Login exitoso"""
    response = client.post(
        "/login",
        data={"username": "david@example.com", "password": "123456"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid_credentials():
    """Test: Login con credenciales inválidas"""
    response = client.post(
        "/login",
        data={"username": "wrong@example.com", "password": "wrongpass"},
    )
    assert response.status_code in [400, 401]


def test_create_order_without_auth():
    """Test: Intentar crear orden sin autenticación"""
    response = client.post(
        "/orders/",
        json={
            "customer_name": "No Auth",
            "total_amount": 100,
        },
    )
    assert response.status_code == 401
