from datetime import date, datetime

class Person:
    def __init__(self,name:str,firstname:str, birthday:str):
        self.name = name
        self.firstname = firstname
        self.birthday = datetime.strptime(birthday,"%d/%m/%Y").date()
        self._age = self.calculate_age()

    def calculate_age(self):
        today = date.today()
        _age = today.year - self.birthday.year
        if(today.month, today.year) < (self.birthday.month, self.birthday.day):
            _age -= 1
        return _age

    def present_yourself(self):
        print(f" Hi! My name is {self.firstname} {self.name} and I am {self._age} years old.")

    def getting_old(self):
        self._age += 1
