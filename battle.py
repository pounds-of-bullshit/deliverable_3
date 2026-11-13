# Battle class for the RPG
from character import Character


class Battle:
    """Manages turn-based combat between 2 Character objects"""
    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the Mage
                    
        Args:
            hero (Character): The hero participating in the battle
            enemy (Character): The enemy participating in the battle
        """
        # Stores the hero and the enemy characters
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Plays 1 round of attacks between the 2 characters"""
        # The round starts only if both characters are alive
        if self.hero.is_alive and self.enemy.is_alive:
            # Lets the hero get the first hit
            self.hero.attack(self.enemy)

            if self.enemy.is_alive:
                # Lets the enemy attack back if they're is still alive
                self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulates battle rounds until 1 character is no longer alive"""
        while self.hero.is_alive and self.enemy.is_alive:
            # Plays the next round
            self.play_round()
