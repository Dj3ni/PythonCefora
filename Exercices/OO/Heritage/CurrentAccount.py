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
        if amount >= self._creditLimit:
            self._balance = amount
        else:
            print("The balance")

    @property
    def credit_limit(self)->float:
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self,amount):
        self._credit_limit = amount