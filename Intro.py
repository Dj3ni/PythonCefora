def maFonction():
        print('Hello')

maFonction()

###########################################################################
# Commentaires
###########################################################################

# docstring: ce qui nous donne accès à des infos en survolant le code
def addition(a,b):
    """
    Cette méthode effectue une addition des variables de la fonction
    :param a:
    :param b:
    :return:
    """
    return a+b

help(addition) # Permet d'afficher la doc de la méthode
print(addition.__doc__) # Idem

###########################################################################
# Imports
###########################################################################

# Importe tout
import math

# Importe un élément d'une librairie
from math import pi

if __name__ == '__main__':
    pi = math.pi
    print(pi)
    pi = math.pi
    print(pi)

