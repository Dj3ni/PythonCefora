class Person:
    next_id = 1

    def __init__(self,firstname:str,lastname:str):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Person.next_id
        Person.next_id += 1

    def __str__(self):
        return f'{self.id}: {self.firstname} {self.lastname}'

    @staticmethod
    def class_description():
        return 'This is a person class'

if __name__ == '__main__':
    print(Person.class_description())

    list_person = [
        Person('James', 'Smith'),
        Person('Scarlett', 'Johansson'),
        Person('Timothée', 'Chalamet')
    ]

    for person in list_person:
        print(person)