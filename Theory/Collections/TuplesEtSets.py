"""
 Les tuples
"""
mon_tuple = (1, 2, 3)

#Destructuration:
print(mon_tuple)
valeur1, valeur2, valeur3 = mon_tuple
print(valeur1, valeur2)

#Accéder à un élément de notre tuple
print(mon_tuple[0])

"""
    Set : ensemble non ordonné d'éléments UNIQUES (contrairement à une liste qui peut avoir plusieurs fois la même valeur) 
"""

animaux = {"chat", "chien","lapin"}

animaux.add("grenouille")
animaux.update(["Lion","Elephant"])
animaux.discard("Lion")
print("chien" in animaux) # permet de checker si un élément est dans le set, renvoie bool

