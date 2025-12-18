"""
    Dictionnaires : clés - valeurs
"""

# Déclaration
student = {
    "name" : "Student",
    "age" : 22,
    "courses" : [
        "Python",
        "C++",
        "Java"],
}

" ou, moins courant "

student2 = dict(
    name="Student2",
    age=22,
    courses=["Python", "Sql", "Java"]
)

"""
    Autrement dit, les clés "name" et "age" viennent des noms des paramètres passés à la fonction.
    
    Et les noms de paramètres en Python :
    
    doivent commencer par une lettre ou un underscore,
    
    ne peuvent pas contenir d’espaces ou de caractères spéciaux,
    
    ne peuvent pas être des nombres.
"""

# Récupération
print(student["courses"])
print(student2["courses"])

for course in student["courses"]:
    print(course)

# Ajouter
student["hobby"] = "boardgames"

# Supprimer
student2.pop("age") #Spécifier quel ensemble clé/valeur supprimer
student2.clear()

# Parcourir
for key, value in student.items():
    print(f"{key} : {value}")
    # NB: Si on récupère un seul objet, on va récupérer le tuple (ensemble clé-valeur)

for key in student.keys():
    print(f"La clé est : {key}")
for value in student.values():
    print(f"La valeur est {value}")