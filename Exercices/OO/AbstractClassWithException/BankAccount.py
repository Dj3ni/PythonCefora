from Person import *
from abc import ABC, abstractmethod
from InvalidAmountException import InvalidAmountException

class BankAccount(ABC):
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

    @abstractmethod
    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
        else:
            print('Amount must be positive')

    @abstractmethod
    def withdraw(self, amount:float):
        if 0 < amount:
            self.balance -= amount
        else:
            raise InvalidAmountException()
            print('amount must be between 0 and balance')

    @abstractmethod
    def transfer(self, amount:float, recipient : BankAccount):
        if 0 < amount:
            self.balance -= amount
        else:
            print('amount must be between 0 and balance')
        recipient.balance += amount

    @abstractmethod
    def calculate_interests(self):
        pass

    @abstractmethod
    def apply_interests(self):
        pass


