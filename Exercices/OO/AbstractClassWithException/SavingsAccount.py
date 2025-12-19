from Exercices.OO.AbstractClassWithException.BankAccount import BankAccount
from Exercices.OO.AbstractClassWithException.Person import *

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

    def deposit(self, amount: float):
        pass

    def transfer(self, amount: float, recipient: BankAccount):
        pass

    def calculate_interests(self):
        """
        Calculate the amount of interests for the savings account
        :return: balance | amount interests
        """
        if self.balance > 0:
            return self.balance * 0.045
        return self.balance

    def apply_interests(self) -> None:
        self.balance += self.calculate_interests()