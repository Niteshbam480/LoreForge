from backend.main import app
from fastapi.testclient import TestClient
import pytest
@pytest.fixture
def client():
    return TestClient(app)
    

@pytest.fixture
def auth_headers(client):
    client.post("/auth/register", json={"email":"test@gmail.com","username":"tester","password":"test20711"})
    response=client.post("/auth/login", json={"email":"test@gmail.com","password":"test20711"})
    token=response.json()["access_token"]
    return {"Authorization":f"Bearer {token}"}



