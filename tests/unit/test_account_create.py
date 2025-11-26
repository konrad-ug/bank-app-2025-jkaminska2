from src.account import Account, BusinessAccount

class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe","93857264539")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "93857264539"
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
    def test_transfer(self):
        account = Account("John", "Doe", "93857264539", None, 5000)
        account.transfer(500)
        assert account.balance == 5500
        account.transfer(-5600)
        assert account.balance == 5500
    def test_przelew_ekspresowy(self):
        account = Account("John", "Doe", "93857264539", None, 5000)
        account.przelewekspresowy(800)
        assert account.balance == 4199
        assert account.history == [-800, -1]
    def test_kredyt(self):
        account = Account("John", "Doe", "93857264539", None, 5000)
        account.transfer(800)
        account.transfer(5600)
        account.transfer(100)
        assert account.submit_for_loan(10000) == True
        account2 = Account("John", "Doe", "93857264539", None, 5000)
        account2.transfer(800)
        account2.transfer(5600)
        assert account2.submit_for_loan(10000) == False
class TestBusinessAccount:
    def test_account(self):
        bus_account = BusinessAccount("Nazwa_firmy", "594837236", 800)
        assert bus_account.nip == "Invalid"
        bus_account.transfer(-500)
        assert bus_account.balance == 300
    def test_przelew_ekspresowy(self):
        bus_account = BusinessAccount("Nazwa_firmy", "5948372366", 800)
        bus_account.przelewekspresowy(800)
        assert bus_account.balance == -5