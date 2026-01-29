import pytest
from unittest.mock import Mock
from src.mongo_repository import MongoAccountsRepository
from src.account import Account

def test_save_all(mocker):
    mock_collection = Mock()
    repo = MongoAccountsRepository.__new__(MongoAccountsRepository)
    repo.collection = mock_collection

    acc = Account("Jan", "Kowalski", "12345678901")
    repo.save_all([acc])

    mock_collection.delete_many.assert_called_once_with({})
    mock_collection.update_one.assert_called_once()

def test_load_all(mocker):
    mock_collection = Mock()
    repo = MongoAccountsRepository.__new__(MongoAccountsRepository)
    repo.collection = mock_collection

    mock_collection.find.return_value = [
        {"first_name": "Jan", "last_name": "Kowalski", "pesel": "12345678901", "balance": 100, "history": []}
    ]

    accounts = repo.load_all()

    assert len(accounts) == 1
    assert isinstance(accounts[0], Account)
    assert accounts[0].balance == 100