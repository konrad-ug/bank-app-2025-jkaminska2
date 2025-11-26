from src.account import Account, BusinessAccount
import pytest
@pytest.fixture
def sample_account():
    account = Account("John", "Doe", "93857264539", None, 5000)
    return account
@pytest.fixture
def sample_business_account():
    bus_account = BusinessAccount("Nazwa_firmy", "594837236", 800)
    return bus_account

class TestAccount:
    def test_account_creation(self, sample_account):
        assert sample_account.first_name == "John"
        assert sample_account.last_name == "Doe"
        assert sample_account.balance == 5000
        assert sample_account.pesel == "93857264539"
    def test_pesel_is_invalid(self):
        account2 = Account("Jane", "Doe", "764")
        assert account2.pesel == "Invalid"
    def test_z_kodem(self):
        account2 = Account("Jane", "Doe", "93857264539","PROM_fjds")
        assert account2.balance==50
    def test_bez_kodu(self):
        account = Account("John", "Doe","93857264539")
        assert account.balance==0
    def test_zly_kod(self):
        account = Account("John", "Doe","93857264539","PRM")
        assert account.balance==0
    def test_senior(self):
        account2 = Account("Jane", "Doe", "50857264539", "PROM_fjds")
        assert account2.balance == 0
class TestTransfer:
    @pytest.mark.parametrize("input,expected", [(1000, 6000), (-500, 4500), (0, 5000)])
    def test_transfer(self,sample_account,input,expected):
        sample_account.transfer(input)
        assert sample_account.balance == expected
    def test_przelew_ekspresowy(self,sample_account):
        sample_account.przelewekspresowy(800)
        assert sample_account.balance == 4199
        assert sample_account.history == [-800, -1]
    def test_kredyt1(self,sample_account):
        sample_account.transfer(800)
        sample_account.transfer(5600)
        sample_account.transfer(100)
        assert sample_account.submit_for_loan(10000) == True
    def test_kredyt2(self,sample_account):
        sample_account.transfer(800)
        sample_account.transfer(5600)
        assert sample_account.submit_for_loan(10000) == False
    def test_kredyt3(self,sample_account):
        sample_account.transfer(800)
        sample_account.transfer(800)
        sample_account.transfer(-800)
        sample_account.transfer(5600)
        sample_account.transfer(5600)
        assert sample_account.submit_for_loan(10000) == True
    def test_kredyt4(self,sample_account):
        sample_account.transfer(800)
        sample_account.transfer(800)
        sample_account.transfer(800)
        sample_account.transfer(560)
        sample_account.transfer(-560)
        assert sample_account.submit_for_loan(1000000) == False
class TestBusinessAccount:
    def test_account(self,sample_business_account):
        assert sample_business_account.nip == "Invalid"
        sample_business_account.transfer(-500)
        assert sample_business_account.balance == 300
        bus_account = BusinessAccount("Nazwa","8574635241")
        assert bus_account.nip == "8574635241"
    def test_przelew_ekspresowy(self,sample_business_account):
        sample_business_account.przelewekspresowy(800)
        assert sample_business_account.balance == -5
    def test_take_loan(self,sample_business_account):
        sample_business_account.transfer(100000)
        sample_business_account.transfer(-1775)
        assert sample_business_account.take_loan(4000) == True
    def test_take_loan2(self,sample_business_account):
        sample_business_account.transfer(10000)
        sample_business_account.transfer(-1775)
        assert sample_business_account.take_loan(400000) == False