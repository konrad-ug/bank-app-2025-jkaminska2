from src.account import Account

def test_condition1_true():
    acc = Account("Jan", "Kowalski", "12345678901")
    acc.history = [10, 20, 30]
    assert acc._condition1() is True

def test_condition1_false():
    acc = Account("Jan", "Kowalski", "12345678901")
    acc.history = [10, -5, 20]
    assert acc._condition1() is False

def test_condition2_true():
    acc = Account("Jan", "Kowalski", "12345678901")
    acc.history = [10, 20, 30, 40, 50]
    assert acc._condition2(100) is True

def test_condition2_false():
    acc = Account("Jan", "Kowalski", "12345678901")
    acc.history = [10, 20, 30, 40, 50]
    assert acc._condition2(200) is False

def test_submit_for_loan_condition1():
    acc = Account("Jan", "Kowalski", "12345678901")
    acc.history = [10, 20, 30]
    assert acc.submit_for_loan(100) is True
    assert acc.balance == 100

def test_submit_for_loan_condition2():
    acc = Account("Jan", "Kowalski", "12345678901")
    acc.history = [10, 20, 30, 40, 50]
    assert acc.submit_for_loan(100) is True
    assert acc.balance == 100