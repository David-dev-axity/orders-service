from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_docs():
    """Test que la documentación está disponible"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_health_check():
    """Test health check endpoint si existe"""
    response = client.get("/")
    # Ajusta según tu endpoint root
    assert response.status_code in [200, 404]
