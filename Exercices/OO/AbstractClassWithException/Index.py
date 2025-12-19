from Exercices.OO.AbstractClassWithException.Person import Person
from Exercices.OO.AbstractClassWithException.SavingsAccount import SavingsAccount
from CurrentAccount import *

p1 = Person("Russel", "Crowe", "15/12/1968")
p2 = Person("Hugh", "Grant", "8/03/1978")
p3 = Person("Scarlett", "Johansson", "26/04/1998")

ac1 = CurrentAccount("BE12 3456 7891 0111", p1,datetime.now(), 1350.00, 1500)
ac2 = CurrentAccount("BE00 1234 5678 9101", p2,datetime.now(),100.00, 2000)
ac3 = CurrentAccount("BE01 2345 6789 1011", p3,datetime.now(),-50.00, 150)

sac1 = SavingsAccount("BE12 3456 7891 0112", p1,datetime.now(),10.000)
sac2 = SavingsAccount("BE00 1234 5678 9102", p2,datetime.now(),100.00)
sac3 = SavingsAccount("BE01 2345 6789 1012", p3,datetime.now(),3500.00)

print(sac2)
print(sac2.balance)
print(sac2.calculate_interests())
print(sac2.apply_interests())
print(sac2.balance)

print(ac2)
print(ac2.balance)
print(ac2.calculate_interests())
print(ac2.apply_interests())
print(ac2.balance)

print(ac3)
print(ac3.balance)
print(ac3.calculate_interests())
print(ac3.apply_interests())
print(ac3.balance)

try:
    ac3.withdraw(50)
except InvalidAmountException as i:
    print(i)