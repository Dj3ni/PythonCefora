from Person import *

class CurrentAccount(object):
    def __init__(self, number: str, balance: float, titular:Person ):
        self._number = number
        self._balance = balance
        self._titular = titular

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print('Balance must be positive')

    @property
    def titular(self):
        return self._titular

    @property
    def number(self):
        return self._number

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            print('Amount must be positive')

    def withdraw(self, amount: float):
        if 0 < amount:
            self.balance -= amount
        else:
            print('amount must be between 0 and balance')

    def transfer(self, amount: float, recipient: CurrentAccount):
        if 0 < amount:
            self.balance -= amount
        else:
            print('amount must be between 0 and balance')
        recipient.balance += amount

