# Imports
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

from colorama import init, Fore, Style
init(autoreset=True)

import random

import time

# combattre ennemi:
    # tant que PV, à chaque tour affiche pv et nom des pokemons
    # quand pokemon KO, passe au suivant
    # quand tous pokemons Ko: vaincus

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

def pick_your_pokemon():
    while True:
        your_pokemon = input("Select your pokemon: ").strip()
        for p in backpack:
            if p["name"].lower() == your_pokemon:
                return p
        print("You don't have that pokemon.")

def hunt_pokemon():
    fighters = []
    hunter = pick_your_pokemon()
    prey = random.choice(pokemons_savage)
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
            print(f"Oh no! {prey["name"]} fled. Try another time!")
    else:
        print(f"Oh no! {hunter["name"]} is KO. Try with another pokemon!")

def heal_pokemons(pokemons):
    for pokemon in pokemons:
        pokemon["hp"] = pokemon["max_hp"]
        print(f"Healing {pokemon['name']}")
    print(f"All your pokemons are healed!")

def fight_pokemons(p1, p2):
    winner = ""
    while winner == "":
        # 1er tour
        if p1["hp"] > 0:
            attack = random.randint(0,p1["attack"]-1) - p2["defense"]
            if attack < 0:
                attack = 0
            p2["hp"] -= attack
            print(f"{p1["name"]} attacks with {attack} damage. {p2["name"]} has  {p2["hp"]} hp left")
            if p2["hp"] <= 0:
                winner = p1["name"]
                print(f"{p2['name']} is KO!")
        time.sleep(0.5)
        if p2["hp"] > 0:
            attack = random.randint(0, p2["attack"] - 1) - p1["defense"]
            if attack < 0:
                attack = 0
            p1["hp"] -= attack
            print(f"{p2["name"]} attacks with {attack} damage. {p1["name"]} has  {p1["hp"]} hp left")
            if p1["hp"] <= 0:
                winner = p2["name"]
                print(f"{p1['name']} is KO!")
        time.sleep(1)
    return winner


def battle(number_of_pokemons = 3):
    my_team = []
    adversary_team = []

    for i in range(number_of_pokemons):
        my_team.append(pick_your_pokemon())
        heal_pokemons(adversary_team)
        adversary_team.append(random.choice(enemy_backpack))

    # Starting the fight ?
    starter = random.randint(1, 2)
    if starter == 1:
        print("You start")
        fight_pokemons(pick_your_pokemon(), adversary_team[0])
    else:
        print("Ennemy starts")
        fight_pokemons(adversary_team[0], pick_your_pokemon())





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
    }
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
            back = input("Go back? ")
            if back == "y":
                continue
        case "2":
            print("Catch a Pokemon")
            hunt_pokemon()
            end_hunt = input("Go back (q) or try again (r)?")
            while end_hunt != "q" or end_hunt == "r":
                if end_hunt == "q":
                    break
                elif end_hunt == "r":
                    hunt_pokemon()
                    end_hunt = input("Go back (q) or try again (r)?")
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
            back = input("Go back? ")
    clear_console()