from Person import *

class BankAccount:
    def __init__(self, account_no : str, titular: Person, last_transaction_date : datetime, balance:float = 0.00):
        self._account_no = account_no
        self._titular = titular
        self.last_transaction_date = last_transaction_date
        self._balance = balance
        self._cash_flow = dict([
            ("balance", self._balance),
            ("transaction_date",self.last_transaction_date)
        ])

    def __str__(self):
        return (f"The account number: {self._account_no}, belongs to : {self._titular.fullname}./n "
                f"The balance is currently: {self._balance} €. The last transaction was : {self.last_transaction_date.date()} at {self.last_transaction_date.time()}")

    @property
    def account_no(self):
        return self._account_no

    @property
    def titular(self):
        return self._titular

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value:float):
        if value > 0:
            self._balance = value
        else:
            print('balance must be positive')

    @property
    def cash_flow(self):
        return {
            "balance": self._balance,
            "transaction_date": self.last_transaction_date
        }

    def deposit(self, amount:float):
        pass

    def withdraw(self, amount:float):
        pass

    def transfer(self, amount:float, recipient : BankAccount):
        pass

