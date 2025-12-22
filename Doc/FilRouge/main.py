from Person import Person
from CurrentAccount import CurrentAccount

person = Person(1,"Doe", "John")
currentAccount = CurrentAccount("BE000000", person)

print(currentAccount.balance)

currentAccount.withdraw(-50)

print(currentAccount.balance)

currentAccount.withdraw(50)

print(currentAccount.balance)

currentAccount.deposite(50)

print(currentAccount.balance)