from datetime import datetime, date

class Person:
    def __init__(self, firstname:str, lastname:str, birthday:str):
        self._firstname = firstname
        self._lastname = lastname
        self._birthday = datetime.strptime(birthday, "%d/%m/%Y").date()
        self.age = self.calculate_age()

    @property
    def fullname(self):
        return f"{self._firstname} {self._lastname}"

    def calculate_age(self):
        """
        Calculate the age of the person from the birthday
        :return :int (age of the person in years)
        """
        today = datetime.today()
        age = today.year - self._birthday.year

        if(today.month, today.year) < (self._birthday.month, self._birthday.year):
            age -= 1
        return age

    def __str__(self):
        return f"{self.fullname} is {self.age} years old."

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname
    @property
    def birthday(self):
        return self._birthday

    