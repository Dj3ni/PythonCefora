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

# Après Héritage
## Créer une classe Epargne permettant la gestion d'un carnet d'épargne devant implémenter:
1. Propriété Publique:
    - Numero (str)
    - solde(float)- lecture seule
    - date dernier retrait(DateTime)
    - Titulaire
2. Méthodes publiques:
    - void Retrait(float Montant)
    - void Depot(float Montant)
## Pour la classe Courant ajouter
Ligne de crédit (float)limite négative strictement supérieure ou égale à 0
## Définir classe Compte reprenant les parties communes entre les 2 autres et utiliser les concepts d'héritage

# Compte abstrait 
1. Définir la classe compte comme étant abstraite
2. Ajouter une méthode à la classe Compte appelée calculIntérêt en sachant que pour un livret épargne, le taux est toujours de 4.5 % mais pour le courant si le solde est positif sera de 3% sinon de 9.75%
3. Ajouter une méthode de la classe compte appelée AppliquerInteret qui additionnera le solde avec le retour de la méthode CalculIntérêt
