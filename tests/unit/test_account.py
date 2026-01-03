from src.account import Account
import pytest

@pytest.fixture
def pesel():
    return "93857264539"

class TestAccount:
    def test_account_creation(self, pesel):
        acc = Account("John", "Doe", pesel, None, 5000)
        assert acc.first_name == "John"
        assert acc.last_name == "Doe"
        assert acc.balance == 5000
        assert acc.pesel == "93857264539"

    def test_pesel_is_invalid(self):
        acc = Account("Jane", "Doe", "764")
        assert acc.pesel == "Invalid"

    def test_with_code(self, pesel):
        acc = Account("Jane", "Doe", pesel, "PROM_fjds")
        assert acc.balance == 50

    def test_without_code(self, pesel):
        acc = Account("John", "Doe", pesel)
        assert acc.balance == 0

    def test_wrong_code(self, pesel):
        acc = Account("John", "Doe", pesel, "PRM")
        assert acc.balance == 0

    def test_senior(self):
        acc = Account("Jane", "Doe", "50857264539", "PROM_fjds")
        assert acc.balance == 0

    def test_bonus_young(self):
        acc = Account("Jane", "Doe", "01010112345", "PROM_X")
        assert acc.balance == 50