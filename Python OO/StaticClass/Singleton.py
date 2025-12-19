from person import Person

class PseudoDB:
    _instance = None
    _is_init = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not PseudoDB._is_init:
            self.list_person = []
            PseudoDB._is_init = True

pseudo_db = PseudoDB()
pseudo_db.list_person.append(Person("John", "Doe"))
pseudo_db.list_person.append(Person("Jane", "Doe"))

pseudo_db = PseudoDB()

for person in pseudo_db.list_person:
    print(person)
