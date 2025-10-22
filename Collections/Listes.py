"""
    Listes : collections modifiables (peuvent contenir des éléments de type différent)
"""
# Init
fruits = ["apple", "banana", "cherry"]

# Accéder
print(fruits[0])

# Ajouter
fruits.append("orange")
fruits.insert(1,"kiwi")
fruits[0]="pineapple"


# Retirer
fruits.remove("orange") # permet de supprimer un élément par sa valeur
fruits.pop() # par défaut retire le dernier
del fruits[0] # permet de supprimer un élément par son index
fruits.clear() # vider la liste

# Valeur >< Référence
copy = fruits.copy() # copie indépendante
newFruits = fruits # copie de référence
list_copied = list(newFruits) # copie de valeur via le constructeur de list()

# Méthodes
fruits.__contains__("orange") # checke si dans la liste ou pas