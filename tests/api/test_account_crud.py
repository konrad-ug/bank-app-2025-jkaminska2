class TestAccountsCRUD:
    def test_create_account(self, client, sample_account):
        r = client.post("/api/accounts", json=sample_account)
        assert r.status_code == 201

    def test_get_account_by_pesel(self, client, sample_account):
        client.post("/api/accounts", json=sample_account)
        r = client.get("/api/accounts/65748392832")
        assert r.status_code == 200
        assert r.get_json() == {
            "balance": 0.0,
            "name": "Jan",
            "pesel": "65748392832",
            "surname": "Kowalski"
        }
        r = client.get("/api/accounts/65748392830")
        assert r.status_code == 404

    def test_update_account(self, client, sample_account):
        client.post("/api/accounts", json=sample_account)
        r = client.patch("/api/accounts/65748392832", json={"name": "Kamil"})
        assert r.status_code == 200

    def test_delete_account(self, client, sample_account):
        client.post("/api/accounts", json=sample_account)
        r = client.delete("/api/accounts/65748392832")
        assert r.status_code == 200

    def test_unique_pesel(self, client, sample_account):
        client.post("/api/accounts", json=sample_account)
        r = client.post("/api/accounts", json=sample_account)
        assert r.status_code == 409