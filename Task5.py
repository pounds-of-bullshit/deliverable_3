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

# Unarmed
hero = Warrior(name="Aria", hp_max=100, damage=10, armor=5)
enemy = Mage(name="Kura", hp_max=100, damage=10, mana=5)

battle = Battle(hero=hero, enemy=enemy)
# Runs rounds until one dies
battle.simulate_battle()

# Finds the winner
winner = hero.name if hero.is_alive else enemy.name
print(f"Winner: {winner}")
print(f"Final HP: {hero.name} = {hero.hp}, {enemy.name} = {enemy.hp}")
print(f"Remaining mana: {enemy.mana}")

# Armed
# Uses the same random rolls each time
random.seed(123)

sword = Weapon(name="Sword", damage_dice=Dice(sides=10))
wand = Weapon(name="Wand", damage_dice=Dice(sides=5))

# The hero and the enemy each equipped with weapons
hero = Warrior(name="Aria", hp_max=100, damage=10, armor=5, weapon=sword)
enemy = Mage(name="Kura", hp_max=100, damage=10, mana=5, weapon=wand)

battle = Battle(hero=hero, enemy=enemy)
battle.simulate_battle()

winner = hero.name if hero.is_alive else enemy.name
print(f"Winner: {winner}")
print(f"Final HP: {hero.name} = {hero.hp}, {enemy.name} = {enemy.hp}")
print(f"Remaining mana: {enemy.mana}")

# 20 battle rounds
# Uses a fixed seed for repeatable results
random.seed(2026)
# Starts the win counters at 0
results = {"Aria": 0, "Kura": 0}

# Runs 20 separate battles
for _ in range(20):
    # Creates a new sword, wand, hero and enemy for each battle
    sword = Weapon(name="Sword", damage_dice=Dice(sides=12)) 
    wand = Weapon(name="Wand", damage_dice=Dice(sides=8))
    hero = Warrior(name="Aria", hp_max=100, damage=10, armor=5, weapon=sword)
    enemy = Mage(name="Kura", hp_max=100, damage=10, mana=5, weapon=wand)
    
    # Sets up the next battle
    battle = Battle(hero=hero, enemy=enemy)
    battle.simulate_battle()

    winner = hero.name if hero.is_alive else enemy.name
    # Adds 1 win to the winner total
    results[winner] += 1

print("Winners of 20 battles:")
# Shows the wins for each character
for name, wins in results.items():
    print(f"{name}: {wins}")