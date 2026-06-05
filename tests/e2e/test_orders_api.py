from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    response = client.post(
        "/login",
        data={"username": "david@example.com", "password": "123456"},
    )

    return response.json()["access_token"]


def test_create_order_e2e():
    token = get_token()

    response = client.post(
        "/orders/",
        json={
            "customer_name": "E2E",
            "total_amount": 300,
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "E2E"
