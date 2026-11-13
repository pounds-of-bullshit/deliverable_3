# code for task 5
import random

from battle import Battle
from character import Character, Mage, Warrior
from dice import Dice
from items import Weapon

# A demonstration of a single battle round
hero = Character(name="Aria", hp_max=100, damage=10)
enemy = Character(name="Kura", hp_max=100, damage=10)
# Sets up the battle
battle = Battle(hero=hero, enemy=enemy)

battle.play_round()
print(f"After 1 round: {hero.name} = {hero.hp} HP, {enemy.name} = {enemy.hp} HP")
