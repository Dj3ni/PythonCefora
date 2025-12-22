class Voiture:
    def __init__(self):
        self.roues = 4

    def avancer(self):
        print("Ma voiture avance")

class Mercedes(Voiture):
    def __init__(self, puissance):
        # passe par le constructeur du parent
        super().__init__()
        self.puissance = puissance

class Bateau:
    def avancer(self):
        print("Mon bateau avance")


# exemple d'héritage multiple
class VoitureAmphibie(Bateau, Voiture):
    def __init__(self):
        Bateau.__init__(self)
        Voiture.__init__(self)
    
    def avancer(self):
        # print("Ma voiture amphibie avance")

        # va recherche la méthode avance du premier parent
        # l'héritage est définit par la première parenthése
        # l'ordre peut être trouver avec VoitureAmphibie.__mro__
        # super().avancer()

        # va chercher spécifiquement la méthode avancer de bateau
        Bateau.avancer(self)



voitureAmphibie = VoitureAmphibie()
print(VoitureAmphibie.__mro__)
voitureAmphibie.avancer()