class Account:
    def __init__(self, first_name, last_name, pesel, kod=None, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.kod = kod
        self.history = []
        if isinstance(pesel,str) and len(pesel) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel
        if isinstance(kod,str) and kod.startswith("PROM_") and self.pesel != "Invalid" and (int(self.pesel[:2]) > 60 or int(self.pesel[:2]) <= 7):
            self.balance += 50
    def transfer(self, kwota):
        if kwota + self.balance >= 0:
            self.balance += kwota
            self.history.append(kwota)
    def przelewekspresowy(self, kwota):
        if self.balance - kwota >= 0:
            self.balance = self.balance - kwota - 1
            self.history.append(kwota * -1)
            self.history.append(-1)
    def submit_for_loan(self, amount):
        if (len(self.history)>=3 and self.history[-1]>0 and self.history[-2]>0 and self.history[-3]>0) or (len(self.history)>=5 and self.history[-1]+self.history[-2]+self.history[-3]+self.history[-4]+self.history[-5] > amount):
            self.balance += amount
            return True
        else:
            return False
class BusinessAccount:
    def __init__(self, company_name, nip, balance = 0):
        self.company_name = company_name
        self.balance = balance
        self.history = []
        if len(nip) != 10:
            self.nip = "Invalid"
        else:
            self.nip = nip
    def transfer(self, kwota):
        if kwota + self.balance >= 0:
            self.balance += kwota
            self.history.append(kwota)
    def przelewekspresowy(self, kwota):
        if self.balance - kwota >= 0:
            self.balance = self.balance - kwota - 5
            self.history.append(kwota * -1)
            self.history.append(-5)