# code for task 1

# A demonstration of the Character class
from character import Character

# Creates an example character without a weapon
ex = Character(name="Aria", hp_max=100, damage=10)
# Prints the character introduction
ex.introduce()

# Displays the character, the starting HP and whether or not they're alive
print(ex)
print(f"Initial HP: {ex.hp}")
print(f"Alive: {ex.is_alive}")

# Tests damage and healing
ex.take_damage(30)
print(f"HP after damage: {ex.hp}")

ex.heal(15)
print(f"HP after healing: {ex.hp}")

# Tests HP boundaries
ex.heal(200)
print(f"HP after excessive healing: {ex.hp}")

ex.take_damage(200)
print(f"HP after excessive damage: {ex.hp}")
print(f"Alive: {ex.is_alive}")
