import pytest
from pytest_mock import MockFixture
from src.account import BusinessAccount

@pytest.fixture
def sample_business_account(mocker):
    mock = mocker.patch("src.account.requests.get")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {
        "result": {"subject": {"statusVat": "Czynny"}}
    }
    return BusinessAccount("Nazwa_firmy", "594837236", 800)

class TestBusinessAccount:
    def test_przelew_ekspresowy(self, sample_business_account):
        sample_business_account.przelewekspresowy(800)
        assert sample_business_account.balance == -5
        assert sample_business_account.przelewekspresowy(800) is False

    def test_transfer(self, sample_business_account):
        assert sample_business_account.outgoing(8000000) is False

    def test_take_loan(self, sample_business_account):
        sample_business_account.incoming(100000)
        sample_business_account.outgoing(1775)
        assert sample_business_account.take_loan(4000) is True

    def test_take_loan2(self, sample_business_account):
        sample_business_account.incoming(10000)
        sample_business_account.outgoing(1775)
        assert sample_business_account.take_loan(400000) is False

    def test_create_company_account(self, mocker: MockFixture):
        mock = mocker.patch("src.account.requests.get")
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {
            "result": {"subject": {"statusVat": "Czynny"}}
        }
        acc = BusinessAccount("Nazwa", "8461627563")
        assert acc.company_name == "Nazwa"
        assert acc.balance == 0
        assert acc.nip == "8461627563"

    def test_business_account_invalid_nip(self, mocker):
        mock = mocker.patch("src.account.requests.get")
        mock.return_value.status_code = 404
        with pytest.raises(ValueError, match="Company not registered!!"):
            BusinessAccount("Firma", "1111111111")