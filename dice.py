# Dice class for the RPG
import random


class Dice:
    """Represents a n-sided dice in the RPG"""
    def __init__(self, sides: int = 6) -> None:
        """"Initialises a dice with a given number of sides (default = 6)"""
        # Rejects it if the dice has fewer than 2 sides
        if sides < 2:
            # An error message for invalid dices 
            raise ValueError("A dice must have at least 2 sides") 
        # Stores n number of sides
        self.sides = sides

    def roll(self) -> int:
        """Rolls the dice and returns a random number between 1 and the number of sides"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Returns a string representation of the dice"""
        # Returns the dice as a readable text
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allows the dice object to be called like a function"""
        # Codereference: https://www.w3schools.com/python/python_magic_call.asp
        # Allows the dice object to roll when called
        return self.roll()