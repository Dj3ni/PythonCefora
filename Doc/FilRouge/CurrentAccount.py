from Person import Person

class CurrentAccount:
    def __init__(self, numberAccount: str, titulaire: Person, balance: float = 0):
        self._numberAccount = numberAccount
        self._titulaire = titulaire
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value: float):
        if value >= 0: 
            self._balance = value
        else:
            print("Le solde ne peut pas être négatif")

    @property
    def titulaire(self):
        return self._titulaire
    
    @property
    def numberAccount(self):
        return self._numberAccount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Montant invalide")
        else:
            self.balance -= amount
    
    def deposite(self, amount: float):
        if amount <= 0:
            print("Montant invalide")
        else:
            self.balance += amount
    
