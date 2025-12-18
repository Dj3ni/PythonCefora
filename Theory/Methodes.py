"""
    Les méthodes
        1. Procédures: ne retournent rien
        2. Fonction: retourne un valeur

"""

# 1. Méthodes intégrées ( incluent dans un langage)

texte = "Hello World"
print(texte.upper())
print(texte.lower())
print(texte.capitalize())
print(texte.replace("Hello", "World"))
print(texte.find("Hello")) #retrouve position de l'élément dans la string
print(texte.__contains__("World")) #vérifie si string contient cet élément (renvoie bool)
print(texte.strip()) #retourne une string épurée de tout espace

texte2 = "Hello World!"
result_split = texte2.split() # Renvoie une liste avec les éléments (par défaut, séparés par un espace)
print(result_split)

result_join = texte2.join(result_split) # prend en paramètre les valeurs à joindre ou directement une liste

print(texte2.isalpha())#sans numéro
print(texte2.isnumeric())#que nums
print(texte2.isalnum())#si alphanumérique

import math

math.sqrt(16) #4
math.pow(2,4) # 16

math.ceil(5.5) # 6
math.floor(5.5) # 5

math.trunc(16)

# fonctions simples sans argument

def nom_fonction():
    texte = "Hello World"
    print(texte)