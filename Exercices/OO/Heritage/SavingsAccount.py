from Exercices.OO.Heritage.BankAccount import BankAccount
from Exercices.OO.Heritage.Person import *

class SavingsAccount(BankAccount):
    def __init__(self, account_no:str, titular : Person, last_transaction_date: datetime, balance:float):
        super().__init__(account_no, titular, last_transaction_date, balance)
        self.balance_start = self.balance


    def withdraw(self, amount) -> None:
        if amount >= self.balance:
            balance_start = self.balance
            self.balance -= amount
            last_transaction_date = datetime.now()
        else:
            print("You don't have enough money to withdraw that amount.")

    def deposit(self, amount):
        self.balance += amount
