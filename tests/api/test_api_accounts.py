import pytest
from app.api import app

def test_create_account(client, sample_account):
    response = client.post("/api/accounts", json=sample_account)
    assert response.status_code == 201
    assert response.get_json()["message"] == "Account created"

def test_get_all_accounts(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    response = client.get("/api/accounts")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["pesel"] == sample_account["pesel"]

def test_get_account_by_pesel(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    response = client.get(f"/api/accounts/{sample_account['pesel']}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == sample_account["name"]
    assert data["surname"] == sample_account["surname"]

def test_get_account_by_pesel_not_found(client):
    response = client.get("/api/accounts/00000000000")
    assert response.status_code == 404

def test_update_account(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    response = client.patch(f"/api/accounts/{sample_account['pesel']}", json={"name": "Adam"})
    assert response.status_code == 200
    updated = client.get(f"/api/accounts/{sample_account['pesel']}")
    assert updated.get_json()["name"] == "Adam"

def test_delete_account(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    response = client.delete(f"/api/accounts/{sample_account['pesel']}")
    assert response.status_code == 200
    response = client.get(f"/api/accounts/{sample_account['pesel']}")
    assert response.status_code == 404

def test_incoming_transfer(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    response = client.post(f"/api/accounts/{sample_account['pesel']}/transfer", json={"type": "incoming", "amount": 100})
    assert response.status_code == 200
    acc = client.get(f"/api/accounts/{sample_account['pesel']}")
    assert acc.get_json()["balance"] == 100

def test_outgoing_transfer_success(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    client.post(f"/api/accounts/{sample_account['pesel']}/transfer", json={"type": "incoming", "amount": 200})
    response = client.post(f"/api/accounts/{sample_account['pesel']}/transfer", json={"type": "outgoing", "amount": 50})
    assert response.status_code == 200
    acc = client.get(f"/api/accounts/{sample_account['pesel']}")
    assert acc.get_json()["balance"] == 150

def test_outgoing_transfer_insufficient_funds(client, sample_account):
    client.post("/api/accounts", json=sample_account)
    response = client.post(f"/api/accounts/{sample_account['pesel']}/transfer", json={"type": "outgoing", "amount": 50})
    assert response.status_code == 422
