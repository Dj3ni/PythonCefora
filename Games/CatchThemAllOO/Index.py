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