import pytest
from src.account import Account

@pytest.fixture
def sample_account():
    return Account("John", "Doe", "93857264539", None, 5000)

@pytest.mark.parametrize("input,expected", [(1000, 6000), (0, 5000)])
def test_transfer(sample_account, input, expected):
    sample_account.incoming(input)
    assert sample_account.balance == expected

class TestTransfers:
    def test_przelew_ekspresowy(self, sample_account):
        sample_account.przelewekspresowy(800)
        assert sample_account.balance == 4199
        assert sample_account.history == [-800, -1]
        assert sample_account.przelewekspresowy(8000000) is False

    def test_loan1(self, sample_account):
        sample_account.incoming(800)
        sample_account.incoming(5600)
        sample_account.incoming(100)
        assert sample_account.submit_for_loan(10000) is True

    def test_loan2(self, sample_account):
        sample_account.incoming(800)
        sample_account.incoming(5600)
        assert sample_account.submit_for_loan(10000) is False

    def test_loan3(self, sample_account):
        sample_account.incoming(800)
        sample_account.incoming(800)
        sample_account.outgoing(800)
        sample_account.incoming(5600)
        sample_account.incoming(5600)
        assert sample_account.submit_for_loan(10000) is True

    def test_loan4(self, sample_account):
        sample_account.incoming(800)
        sample_account.incoming(800)
        sample_account.incoming(800)
        sample_account.incoming(560)
        sample_account.outgoing(560)
        assert sample_account.submit_for_loan(1000000) is False