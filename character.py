# Character class for the RPG
# Most of the code is from the original game_simulator_v1.py file
from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character
    
        Args:
            name (str): The name of the character
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): The weapon the character wields (default = None)
        """
        # Stores the name, maximum HP, base attack damage and weapon
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Reduces the character's HP by the given damage amount"""
        # Makes sure that the HP doesn't go below 0
        self._hp = max(self._hp - max(amount, 0), 0)

    def heal(self, amount: int) -> None:
        """Increases the character's HP by the given amount"""
        # Restores HP without going over the maximum
        self._hp = min(self._hp + max(amount, 0), self.hp_max)
    
    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character"""
        # Uses weapon damage if the character is equipped with a weapon 
        if self.weapon is not None:
            # Rolls the weapon damage
            damage = self.weapon.roll_damage()
        else:
            # Uses the base damage if unequipped 
            damage = self.damage

        # Deals damage to the target character 
        target.take_damage(damage)
    
    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")
    
    def __repr__(self) -> str:
        """Representation of character object"""
        # Returns a detailed character description
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"
    
    def __str__(self) -> str:
        """String representation of character object"""
        # Returns a more readable description
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"
    
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        # Returns the current HP
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Returns True if the character is alive, otherwise False"""
        # Checks whether the HP is above 0
        return self._hp > 0
