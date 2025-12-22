class Fruit:
    def __init__(self, nom):
        self.nom = nom


class Panier:
    def __init__(self):
        self.fruits = []

    # pour le +=
    def __iadd__(self, fruit):
        if  not isinstance(fruit, Fruit):
            print("Ce n'est pas un fruit")
        else:
            self.fruits.append(fruit)
        return self
    
    # pour le -=
    def __isub__(self, fruit):
        if  not isinstance(fruit, Fruit):
            print("Ce n'est pas un fruit")
        elif fruit in self.fruits:
            self.fruits.remove(fruit)
        return self
    
    # lecture du fruit en position index de la liste
    def __getitem__(self, index):
        if index < 0 and index >= len(self.fruits):
            print("Index invalid")
        else:
            return self.fruits[index] 
       
    # Définission du fruit en position index de la liste 
    def __setitem__(self, index, value):
        if index < 0 and index >= len(self.fruits):
            print("Index invalid")
        else:
            self.fruits[index] = value
    
    
    
panier = Panier()
pomme = Fruit("Pomme")

panier += pomme
panier += Fruit("Banane")
panier += Fruit("Kiwi")
panier -= pomme

for fruit in panier.fruits:
    print(fruit.nom)

index = 1
print(f"le fruit en position {index} est {panier[index].nom}")

panier[index] = Fruit("Fraise")
print(f"le fruit en position {index} est {panier[index].nom}")