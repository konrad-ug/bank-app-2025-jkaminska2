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
    def _condition1(self):
        if len(self.history) >= 3 and self.history[-1] > 0 and self.history[-2] > 0 and self.history[-3] > 0:
            return True
        return False
    def _condition2(self,amount):
        if len(self.history) >= 5 and self.history[-1] + self.history[-2] + self.history[-3] + self.history[-4] + self.history[-5] > amount:
            return True
        return False
    def submit_for_loan(self,amount):
        if self._condition1()==True or self._condition2(amount)==True:
            self.balance += amount
            self.history.append(amount)
            return True
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
    def take_loan(self,amount):
        if self.balance >= amount * 2 and -1775 in self.history:
            self.balance += amount
            self.history.append(amount)
            return True
        return False