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
