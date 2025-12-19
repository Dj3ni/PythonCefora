from BankAccount import *

class CurrentAccount(BankAccount):

    def __init__(self, account_no:str, titular :Person, last_transaction_date : datetime, balance:float, credit_limit:float ):
        super().__init__(account_no, titular, last_transaction_date, balance)
        self._credit_limit = credit_limit

    @property
    def balance(self)->float:
        return self.balance

    @balance.setter
    def balance(self, amount)->None:
        if amount >= self._credit_limit:
            self._balance = amount
        else:
            print("The balance must be positive")

    @property
    def credit_limit(self)->float:
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self,amount):
        self._credit_limit = amount

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def transfer(self, amount:float, recipient : BankAccount):
        pass

    def calculate_interests(self):
        if self.balance > 0:
            return self.balance * 0.03

        if self.balance < 0:
            return self.balance * 0.0975
        return self.balance

    def apply_interests(self):
        if self.balance > 0:
            self.balance += self.calculate_interests()
        if self.balance < 0:
            self.balance -= self.calculate_interests()
