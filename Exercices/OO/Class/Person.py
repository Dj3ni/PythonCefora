class Person:
    def __init__(self, firstname:str, lastname:str):
        self._firstname = firstname
        self._lastname = lastname
        self._id = id

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self,value):
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self,value):
        self._lastname = value

    @property
    def id(self):
        return self._id