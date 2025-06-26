import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    email = "test@example.com"
    password = "strongpassword"

    # Registrar usuário
    response = client.post("/auth/register", json={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json()["email"] == email

    # Login
    response = client.post("/auth/login", data={"username": email, "password": password})
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens
