
livres = []

livre = dict(
    id = 0,
    isbn="",
    title="",
    author="",
    editor="",
)




# Ajouter, supprimer, afficher la liste

def add_livre(livre):
    livres.append(livre)



for livre in livres:
    if livre["id"] == 0:
        del livres[livre["id"]]