class Account:
    def __init__(self, first_name, last_name, pesel, kod=None, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.kod = kod
        if isinstance(pesel,str) and len(pesel) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel
        if isinstance(kod,str) and kod.startswith("PROM_") and self.pesel != "Invalid" and (int(self.pesel[:2]) > 60 or int(self.pesel[:2]) <= 7):
            self.balance += 50
    def transfer(self, kwota):
        if kwota + self.balance >= 0:
            self.balance += kwota
class BusinessAccount:
    def __init__(self, company_name, nip, balance = 0):
        self.company_name = company_name
        self.balance = balance
        if len(nip) != 10:
            self.nip = "Invalid"
        else:
            self.nip = nip
    def transfer(self, kwota):
        if kwota + self.balance >= 0:
            self.balance += kwota