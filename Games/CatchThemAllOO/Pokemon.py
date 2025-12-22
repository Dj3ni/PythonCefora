from PokeType import PokeType
from colorama import init, Fore, Style
init(autoreset=True)

class Pokemon:
    type_colors = {
        "electric": Fore.YELLOW,
        "poison": Fore.MAGENTA,
        "fire": Fore.RED,
        "water": Fore.BLUE,
        "grass": Fore.GREEN,
        "ground": Fore.LIGHTGREEN_EX,
        "ghost": Fore.WHITE,
    }
    def __init__(self,name:str,hp:int,max_hp:int, attack:int, defense:int,speed:int, type:PokeType):
        self._name = name
        self.hp = hp
        self._max_hp = max_hp
        self._attack = attack
        self._defense = defense
        self._speed = speed
        self._type = type

    def display_pokemon(self):
        color = self.type_colors[self._type.name.lower()] if self._type.name.lower() in self.type_colors.keys() else Fore.WHITE,

        # Display Poke info
        print(f"{color}{Style.BRIGHT}┌{'─' * 20}┐")
        print(f"{color}{Style.BRIGHT}│ Name: {self._name:<13}│")
        print(f"{color}{Style.BRIGHT}│ Type: {self._type:<13}│")
        print(f"{color}{Style.BRIGHT}│ HP: {self.hp:<15}│")
        print(f"{color}{Style.BRIGHT}│ Attack: {self._attack:<11}│")
        print(f"{color}{Style.BRIGHT}│ Defense: {self._defense:<10}│")
        print(f"{color}{Style.BRIGHT}│ Speed: {self._speed:<12}│")
        print(f"{color}{Style.BRIGHT}└{'─' * 20}┘{Style.RESET_ALL}")