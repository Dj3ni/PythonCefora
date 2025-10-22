import random

# Inits :
colors = ["a", "b", "c", "d", "e", "f"]
CODE_LENGTH = 4
mystery_combination = random.choices(colors, k = CODE_LENGTH)
print(mystery_combination)
user_combination = [] # Pour enregistrer l'essai du user et lui donner un feedback
correct_colors = []
correct_colors_placement = []


# 1. Check si valide

def check_if_valid(guess):
    """
    Checks if the guess is valid
    :param guess: string
    :return: bool
    """
    combination = list(guess)

    if len(combination) != 4:
        print("You mist pick 4 colors!")
        return False

    for letter in combination:
        if letter not in colors:
            print("Your colors must be a b c d e f.")
            return False
    return True

# 2. Check Couleur
def check_color(guess, code):
    correct_colors.clear()
    for i in range(CODE_LENGTH):
        if code[i] != guess[i] and guess[i] in code:
            if guess[i] not in correct_colors:
                correct_colors.append(guess[i])
    return len(correct_colors)

# 3. Check Couleur / Position
def check_color_position(guess, code):
    correct_colors_placement.clear()
    for i in range(CODE_LENGTH):
        if guess[i] == code[i]:
            correct_colors_placement.append(guess[i])
    return len(correct_colors_placement)

# 4. Check Code
def check_code(guess, code):
    color_counter = check_color(guess, code)
    place_counter = check_color_position(guess, code)

    print(f" There is {color_counter} good colors and {place_counter} in a good position.")


# Programme

print("Welcome to Mastermind!")
user_guess = ""
attempts = 0

while list(user_guess) != mystery_combination and attempts < 10:
    user_guess = input("Pick a combination of 4 colors between a b c d e f : ")

    while not check_if_valid(user_guess):
        user_guess = input("Pick a combination of 4 colors between a b c d e f : ")

    user_combination = list(user_guess)
    check_code(user_combination, mystery_combination)
    attempts += 1
    print(f"You have {10-attempts} attempts left.")

if user_combination != mystery_combination and attempts == 10:
    print(f"Such a pity! The good combination was {mystery_combination}.\nThank you for playing! ")
elif user_combination == mystery_combination and attempts <= 10:
    print(f"You won in {attempts} attempts! The combination was {mystery_combination} \nThank you for playing!")