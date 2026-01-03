import pytest
from app.api import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def sample_account():
    return {
        "name": "Jan",
        "surname": "Kowalski",
        "pesel": "65748392832"
    }

@pytest.fixture(autouse=True)
def clear_registry():
    from app.api import registry
    registry.accounts = []