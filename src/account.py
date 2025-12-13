import requests
import os
from datetime import datetime
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
    def incoming(self, kwota):
        self.balance += kwota
        self.history.append(kwota)
        return True
    def outgoing(self, kwota):
        if self.balance - kwota >= 0:
            self.balance -= kwota
            self.history.append(kwota * -1)
            return True
        return False
    def przelewekspresowy(self, kwota):
        if self.balance - kwota >= 0:
            self.balance = self.balance - kwota - 1
            self.history.append(kwota * -1)
            self.history.append(-1)
            return True
        return False
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
class BusinessAccount: # pragma: no cover
    def __init__(self, company_name, nip, balance = 0):
        self.company_name = company_name
        self.balance = balance
        self.history = []
        if len(nip) != 10:
            self.nip = "Invalid"
        else:
            date = datetime.today().strftime('%Y-%m-%d')
            BANK_APP_MF_URL = os.getenv("BANK_APP_MF_URL")
            r = requests.get(f"{BANK_APP_MF_URL}api/search/nip/{nip}?date={date}")
            if r.status_code == 200:
                self.nip = nip
            else:
                raise ValueError("Company not registered!!")
    def incoming(self, kwota):
        self.balance += kwota
        self.history.append(kwota)
        return True
    def outgoing(self, kwota):
        if self.balance - kwota >= 0:
            self.balance -= kwota
            self.history.append(kwota * -1)
            return True
        return False
    def przelewekspresowy(self, kwota):
        if self.balance - kwota >= 0:
            self.balance = self.balance - kwota - 5
            self.history.append(kwota * -1)
            self.history.append(-5)
            return True
        return False
    def take_loan(self,amount):
        if self.balance >= amount * 2 and -1775 in self.history:
            self.balance += amount
            self.history.append(amount)
            return True
        return False
    def status_vat(self, nip):
        date = datetime.today().strftime('%Y-%m-%d')
        BANK_APP_MF_URL = os.getenv("BANK_APP_MF_URL")
        print(f"Sending requests to {BANK_APP_MF_URL}")
        r = requests.get(f"{BANK_APP_MF_URL}api/search/nip/{nip}?date={date}")
        if r.status_code == 200:
            data = r.json()
            if data.result.subject["statusVat"] == "Czynny":
                print("Status Vat: Czynny")
                return True
            print("Status Vat: Nieczynny")
            return False
        print("Błąd")
        return False

class AccountRegistry:
    def __init__(self):
        self.accounts=[]
    def add_account(self,account: Account):
        self.accounts.append(account)
    def search_account(self,pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
    def accounts_list(self):
        return self.accounts
    def accounts_counter(self):
        return len(self.accounts)