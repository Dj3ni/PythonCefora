# Imports
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

from colorama import init, Fore, Style
init(autoreset=True)

import random
import time

# Data
pokemons_savage = [
    {
        "name": "Charmander",
        "hp": 39,
        "max_hp": 40,
        "attack": 52,
        "defense": 43,
        "speed": 65,
        "type": "fire"
    },
    {
        "name": "Squirtle",
        "hp": 44,
        "max_hp": 50,
        "attack": 48,
        "defense": 65,
        "speed": 43,
        "type": "water"
    },
    {
        "name": "Bulbasaur",
        "hp": 45,
        "max_hp": 50,
        "attack": 49,
        "defense": 49,
        "speed": 45,
        "type": "grass"
    },
    {
        "name": "Eevee",
        "hp": 55,
        "max_hp": 60,
        "attack": 55,
        "defense": 50,
        "speed": 55,
        "type": "normal"
    },
    {
        "name": "Jigglypuff",
        "hp": 115,
        "max_hp": 120,
        "attack": 45,
        "defense": 20,
        "speed": 20,
        "type": "fairy"
    },
    {
        "name": "Geodude",
        "hp": 40,
        "max_hp": 40,
        "attack": 80,
        "defense": 100,
        "speed": 20,
        "type": "rock"
    },
    {
        "name": "Abra",
        "hp": 25,
        "max_hp": 30,
        "attack": 20,
        "defense": 15,
        "speed": 90,
        "type": "psychic"
    },
    {
        "name": "Gastly",
        "hp": 30,
        "max_hp": 30,
        "attack": 35,
        "defense": 30,
        "speed": 80,
        "type": "ghost"
    },
    {
        "name": "Machop",
        "hp": 70,
        "max_hp": 70,
        "attack": 80,
        "defense": 50,
        "speed": 35,
        "type": "fighting"
    }
]
backpack = [
    {
        "name": "Pikachu",
        "hp": 50,
        "max_hp": 50,
        "attack": 50,
        "defense": 30,
        "speed": 10,
        "type": "electric"
    },
{
        "name": "Ponyta",
        "hp": 50,
        "max_hp": 50,
        "attack": 85,
        "defense": 55,
        "speed": 90,
        "type": "fire"
    },
{
        "name": "Squirtle",
        "hp": 44,
        "max_hp": 50,
        "attack": 48,
        "defense": 65,
        "speed": 43,
        "type": "water"
    },

]
enemy_backpack = [
    {
        "name": "Vulpix",
        "hp": 38,
        "max_hp": 40,
        "attack": 41,
        "defense": 40,
        "speed": 65,
        "type": "fire"
    },
    {
        "name": "Oddish",
        "hp": 45,
        "max_hp": 50,
        "attack": 50,
        "defense": 55,
        "speed": 30,
        "type": "grass"
    },
    {
        "name": "Sandshrew",
        "hp": 50,
        "max_hp": 50,
        "attack": 75,
        "defense": 85,
        "speed": 40,
        "type": "ground"
    },
    {
        "name": "Poliwag",
        "hp": 40,
        "max_hp": 40,
        "attack": 50,
        "defense": 40,
        "speed": 90,
        "type": "water"
    },
    {
        "name": "Magnemite",
        "hp": 25,
        "max_hp": 30,
        "attack": 35,
        "defense": 70,
        "speed": 45,
        "type": "electric"
    },
    {
        "name": "Cubone",
        "hp": 50,
        "max_hp": 50,
        "attack": 50,
        "defense": 95,
        "speed": 35,
        "type": "ground"
    },
    {
        "name": "Koffing",
        "hp": 40,
        "max_hp": 40,
        "attack": 65,
        "defense": 95,
        "speed": 35,
        "type": "poison"
    },
    {
        "name": "Seel",
        "hp": 65,
        "max_hp": 70,
        "attack": 45,
        "defense": 55,
        "speed": 45,
        "type": "water"
    },
    {
        "name": "Ponyta",
        "hp": 50,
        "max_hp": 50,
        "attack": 85,
        "defense": 55,
        "speed": 90,
        "type": "fire"
    },
    {
        "name": "Bellsprout",
        "hp": 50,
        "max_hp": 50,
        "attack": 75,
        "defense": 35,
        "speed": 40,
        "type": "grass"
    }
]
type_colors = {
    "electric": Fore.YELLOW,
    "poison": Fore.MAGENTA,
    "fire": Fore.RED,
    "water": Fore.BLUE,
    "grass": Fore.GREEN,
    "ground": Fore.LIGHTGREEN_EX,
    "ghost": Fore.WHITE,
}

# Methods
def open_backpack():
    for pokeball in backpack:
        display_pokemon(pokeball)

def display_pokemon(pokemon):
    color = type_colors.get(pokemon["type"], Fore.WHITE)

    # Display Poke info
    print(f"{color}{Style.BRIGHT}┌{'─' * 20}┐")
    print(f"{color}{Style.BRIGHT}│ Name: {pokemon['name']:<13}│")
    print(f"{color}{Style.BRIGHT}│ Type: {pokemon['type']:<13}│")
    print(f"{color}{Style.BRIGHT}│ HP: {pokemon['hp']:<15}│")
    print(f"{color}{Style.BRIGHT}│ Attack: {pokemon['attack']:<11}│")
    print(f"{color}{Style.BRIGHT}│ Defense: {pokemon['defense']:<10}│")
    print(f"{color}{Style.BRIGHT}│ Speed: {pokemon['speed']:<12}│")
    print(f"{color}{Style.BRIGHT}└{'─' * 20}┘{Style.RESET_ALL}")

def open_pokedex():
    for pokemon in pokemons_savage:
        display_pokemon(pokemon)

def pick_your_pokemon(poke_list):
    while True:
        your_pokemon = input("Select your pokemon: ").strip()
        for p in poke_list:
            if p["name"].lower() == your_pokemon.lower():
                if p["hp"] > 0:
                    return p
                print(f"{p['name']} is too tired, pick another one")
        print("You don't have that pokemon.")

def hunt_pokemon():
    fighters = []
    prey = random.choice(pokemons_savage)
    print("You encountered : ")
    display_pokemon(prey)
    hunter = pick_your_pokemon(backpack)
    fighters.append([hunter, prey])

    display_pokemon(hunter)
    display_pokemon(prey)

    if hunter["hp"] > 0:
        if hunter["attack"] > prey["defense"]:
            print("You caught it!")
            if prey["name"] in backpack:
                prey["name"]+= 1
            backpack.append(prey)
        else:
            print(f"Oh no! {prey['name']} fled. Try another time!")
    else:
        print(f"Oh no! {hunter['name']} is KO. Try with another pokemon!")

def heal_pokemons(pokemons):
    for pokemon in pokemons:
        if pokemon["hp"] < pokemon["max_hp"]:
            pokemon["hp"] = pokemon["max_hp"]
            print(f"Healing {pokemon['name']}")
    print(f"All pokemons are healed!")

# Fight methods :
    # tant que PV, à chaque tour affiche pv et nom des pokemons
    # quand pokemon KO, passe au suivant
    # quand tous pokemons Ko: vaincus

def fight_pokemons(p1, p2):
    while p1["hp"] > 0 and p2["hp"] > 0:
        # If attacker put defender KO, return his name as winner
        if deal_damage(p1, p2):
            return p1["name"]
        time.sleep(0.5)

        # Otherwise defender's turn, if he puts attacker KO, his name is returned
        if deal_damage(p2,p1):
            return p2["name"]
        time.sleep(0.5)

def deal_damage(attacker, defender):
    if attacker["hp"] > 0:
        attack = random.randint(0,attacker["attack"]-1) - defender["defense"]
        if attack < 0:
            attack = 0
        defender["hp"] -= attack
        print(f"{attacker['name']} attacks with {attack} damage. {defender['name']} has  {defender['hp']} hp left")
        if defender["hp"] <= 0:
            print(f"{defender['name']} is KO!, {attacker['name']} won the fight!")
            return True
    return False

def team_battle(my_team, adversary_team):
    current_enemy = adversary_team[0]
    while len(my_team) > 0 and len(adversary_team) > 0:
        print(my_team)
        my_pokemon = pick_your_pokemon(my_team)

        starter = random.randint(1, 2)
        if starter == 1:
            print("You start")
            fight_pokemons(my_pokemon, current_enemy)
        else:
            print("Enemy starts")
            fight_pokemons(current_enemy, my_pokemon)
        if my_pokemon["hp"] == 0 :
            my_team.remove(my_pokemon)
        else:
            adversary_team.pop(0)
            current_enemy = adversary_team[0]
    return "You win!" if len(my_team) > 0  else "Enemy wins!"

def battle(number_of_pokemons = 3):
    if len(backpack) < number_of_pokemons:
        return print(f"You must at least have {number_of_pokemons} pokemons to start a fight!")

    my_team = []
    adversary_team = []

    print(f"First, you need to build a team of {number_of_pokemons} pokemons:")

    for i in range(number_of_pokemons):
        my_team.append(pick_your_pokemon(backpack))
        adversary_team.append(random.choice(enemy_backpack))

    heal_pokemons(adversary_team)
    print("Let's start the fight!")

    winner = team_battle(my_team,adversary_team)
    print(winner)


# Program
user_input = ""

while user_input != "q":
    print("Welcome to the CatchThemAll!")
    print("What would you like to do?")
    print("1 - Open my backpack")
    print("2 - Catch a Pokemon")
    print("3 - Fight!")
    print("4 - Heal my pokemons")
    print("5 - Open your Pokedex")
    print("q - Quit")

    user_input = input("Enter your choice: ")
    clear_console()
    match user_input:
        case "1":
            print("Opening your backpack")
            open_backpack()
            back = input("Go back? y/n")
            if back == "y":
                continue
        case "2":
            print("Catch a Pokemon")
            hunt_pokemon()
            end_hunt = input("Go back (q) or try again (r)?")
            while end_hunt != "q":
                if end_hunt == "r":
                    hunt_pokemon()
                    end_hunt = input("Go back (q) or try again (r)?")
                #end_hunt = input("Go back (q) or try again (r)?")
        case "3":
            print("Fight!")
            battle()
            #fight_pokemons(backpack[0],enemy_backpack[0])
        case "4":
            print("Heal my pokemons")
            heal_pokemons(backpack)
        case "5":
            print("Opening your Pokedex")
            open_pokedex()
    clear_console()
print("Thanks for these great adventures, see you later!")

