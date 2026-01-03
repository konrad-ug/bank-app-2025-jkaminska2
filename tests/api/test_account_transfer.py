class TestAccountTransfer:
    def test_transfer(self, client, sample_account):
        client.post("/api/accounts", json=sample_account)
        r = client.post("/api/accounts/65748392832/transfer", json={"amount": 500, "type": "incoming"})
        assert r.status_code == 200

        r = client.post("/api/accounts/65748392832/transfer", json={"amount": 5000, "type": "outgoing"})
        assert r.status_code == 422

        r = client.post("/api/accounts/65748392832/transfer", json={"amount": 5000, "type": "???"})
        assert r.status_code == 404

        r = client.post("/api/accounts/65748392832/transfer", json={"amount": 5000})
        assert r.status_code == 404