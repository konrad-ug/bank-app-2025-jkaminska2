from src.account import Account

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