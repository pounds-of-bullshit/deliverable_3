# code for task 3
from character import Character
from dice import Dice
from items import Weapon

# A demonstration of the Weapon class

# Creates 2 weapons with different damage dice
sword = Weapon(name="Sword", damage_dice=Dice(sides=7))
axe = Weapon(name="Axe", damage_dice=Dice(sides=10))

print(f"{sword.name}: {sword.roll_damage()} damage")
print(f"{axe.name}: {axe.roll_damage()} damage")

# Compares armed and unarmed characters
armed = Character(name="Aria", weapon=sword)
unarmed = Character(name="Kura", damage=100)

# Creates the 2 targets
target1 = Character(name="Target 1")
target2 = Character(name="Target 2")
# Attacks the first target using weapon damage
armed.attack(target1)
# Attacks the second target using base damage
unarmed.attack(target2)

print(f"HP after weapon attack: {target1.hp}")
print(f"HP after base attack: {target2.hp}")