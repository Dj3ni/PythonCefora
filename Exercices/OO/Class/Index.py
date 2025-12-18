from Person import *
from CurrentAccount import *

p1 = Person("John", "Doe")
p2 = Person("Hugh", "Grant")
p3 = Person("Scarlett", "Johansson")

ac1 = CurrentAccount("BE12 3456 7891 0111", 0.00, p1)
ac2 = CurrentAccount("BE00 1234 5678 9101", 100.00, p2)
ac3 = CurrentAccount("BE01 2345 6789 1011", 50.00, p3)

ac1.deposit(10)
ac1.deposit(20)
ac1.deposit(30)
ac1.deposit(40)

print(ac1.balance)

ac1.withdraw(50)

print(ac1.balance)

ac1.transfer(10.00, ac2)

print(ac1.balance)
print(ac2.balance)

ac2.transfer(4.00, ac3)
print(ac2.balance)
print(ac3.balance)

print(f"{ac3.titular.firstname} {ac3.titular.lastname}")

