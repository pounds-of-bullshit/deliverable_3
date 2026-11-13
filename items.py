# Weapon class for the RPG
from dice import Dice


class Weapon:
    """Represents a weapon used by characters in the RPG"""
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Initialises a weapon with a name and damage dice"""
        # Stores the weapon name and the dice used for weapon damage
        self.name = name
        self.damage_dice = damage_dice 

    def roll_damage(self) -> int:
        """Rolls the damage dice and returns the result"""
        # Rolls the dice to calculate weapon damage
        return self.damage_dice.roll()