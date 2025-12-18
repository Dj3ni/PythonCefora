# Créer des Personnes

Attributs:
 - Id
 - Nom
 - Prenom

# Créer des comptes courants

Attributs:
 - numéro
 - titulaire : Person
 - solde

Comportement: 
 - Retrait (somme)
 - Depôt (somme)
 - Virement (vers Personnes)

Contrainte:
 - Pas de retrait / dépôt négatif
 - Retrait ne doit pas amener à un solde négatif.