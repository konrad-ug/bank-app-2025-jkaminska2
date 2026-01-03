import pytest
from pytest_mock import MockFixture
from src.account import Account, BusinessAccount

@pytest.fixture
def mock_smtp(mocker: MockFixture):
    return mocker.patch("src.account.SMTPClient")

@pytest.fixture
def mock_nip(mocker):
    mock = mocker.patch("src.account.requests.get")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {
        "result": {"subject": {"statusVat": "Czynny"}}
    }
    return mock

def test_send_history_personal_success(mock_smtp):
    mock_smtp.return_value.send.return_value = True
    acc = Account("Jan", "Kowalski", "65748392832")
    acc.history = [100, -1, 500]
    result = acc.send_history_via_email("test@example.com")
    assert result is True
    mock_smtp.return_value.send.assert_called_once()
    subject, text, email = mock_smtp.return_value.send.call_args[0]
    assert "Account Transfer History" in subject
    assert text == "Personal account history: [100, -1, 500]"
    assert email == "test@example.com"

def test_send_history_personal_fail(mock_smtp):
    mock_smtp.return_value.send.return_value = False
    acc = Account("Jan", "Kowalski", "65748392832")
    acc.history = [1, 2, 3]
    result = acc.send_history_via_email("x@example.com")
    assert result is False

def test_send_history_business_success(mock_smtp, mock_nip):
    mock_smtp.return_value.send.return_value = True
    acc = BusinessAccount("Firma", "1234567890")
    acc.history = [5000, -1000, 500]
    result = acc.send_history_via_email("biz@example.com")
    assert result is True
    mock_smtp.return_value.send.assert_called_once()
    subject, text, email = mock_smtp.return_value.send.call_args[0]
    assert "Account Transfer History" in subject
    assert text == "Company account history: [5000, -1000, 500]"
    assert email == "biz@example.com"

def test_send_history_business_fail(mock_smtp, mock_nip):
    mock_smtp.return_value.send.return_value = False
    acc = BusinessAccount("Firma", "1234567890")
    acc.history = [1, 2, 3]
    result = acc.send_history_via_email("biz@example.com")
    assert result is False