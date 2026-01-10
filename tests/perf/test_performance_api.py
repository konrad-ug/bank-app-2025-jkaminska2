import time
import pytest
from app.api import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client
@pytest.fixture(autouse=True)
def clear_registry():
    from app.api import registry
    registry.accounts = []

class TestPerformanceApi:
    def test_create_delete_100_times(self, client):
        for i in range(100):
            payload = {
                "name" : "Jan",
                "surname": "Kowalski",
                "pesel" : f"900000000{i:02d}"
            }
            start = time.time()
            r = client.post("/api/accounts", json=payload)
            duration = time.time() - start
            assert r.status_code == 201
            assert duration < 0.5

            start = time.time()
            r = client.delete(f"/api/accounts/{payload['pesel']}")
            duration = time.time() - start
            assert r.status_code == 200
            assert duration < 0.5

    def test_100_incoming_transfers(self, client):
        payload = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "12345678910"
        }
        r = client.post("/api/accounts", json=payload)
        assert r.status_code == 201
        for i in range(100):
            start = time.time()
            r = client.post("/api/accounts/12345678910/transfer", json={"amount": 100, "type": "incoming"})
            duration = time.time() - start
            assert r.status_code == 200
            assert duration < 0.5
        r = client.get("/api/accounts/12345678910")
        assert r.status_code == 200
        assert r.get_json()["balance"] == 10000
