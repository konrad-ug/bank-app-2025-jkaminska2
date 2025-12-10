import pytest
from app.api import app, registry
@pytest.fixture
def client():
    app.config["TESTING"] = True
    registry.accounts = []
    with app.test_client() as client:
        yield client

def test_create_account(client):
    response = client.post("/api/accounts", json = {
        "name": "Jan",
        "surname": "Kowalski",
        "pesel": "65748392832"
    })
    assert response.status_code == 201