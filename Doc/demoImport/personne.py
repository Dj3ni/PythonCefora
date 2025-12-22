class Personne:
    # équivalent du constructeur
    # permet de définir les premières valeurs
    def __init__(self, nom: str, prenom: str, age: int):
        self._nom = nom
        self._prenom = prenom
        self._age = age

    # propriété et accesseur (rendre la valeur accessible en lecture)
    @property
    def age(self):
        return self._age
    
    # mutateur (rendre modifiable la valeur)
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value

    # Fonction donnant les informations de notre instance de Personne
    def presenter(self):
        return f"{self._prenom} {self._nom} {self._age} ans"
    
    # Procédure vieillissant notre instance de Personne
    def vieillir(self):
        self._age += 1

    # définit le retour lors de l'utilisation du print(), format() et str()
    def __str__(self):
        return f"{self._prenom} {self._nom} {self._age} ans"

def saluer():
    print("Hello world")

if __name__ == "__main__":
    print("Depuis le fichier personne")
    personne = Personne("Doe", "John", 42)
    # personne.vieillir()
    # personne.age = -5
    # print(personne.presenter())


    # print(Personne.__class__)
    # print(Personne.__name__)

    # tuples avec les classes parentes (tout est objet)
    # print(Personne.__bases__)
    # print(str.__bases__)

    # dictionnaire des attributs et méthodes
    # print(Personne.__dict__)

    print(personne)