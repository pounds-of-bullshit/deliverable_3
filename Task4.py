# code for task 4
from character import Character, Mage, Warrior

# A demonstration of the subclasses

# Warrior
warrior = Warrior(name="Aria", hp_max=100, armor=5)
# Applies damage after armor reduction
warrior.take_damage(20)
print(f"Aria's HP after 20 incoming damage: {warrior.hp}")

# Mage
mage = Mage(name="Kura", hp_max=100, damage=10, mana=30)
target = Character(name="Target", hp_max=150)

# Tests out 5 mage attacks
for turn in range(1, 6):
    # Attacks and update the mage's mana
    mage.attack(target)
    print(f"Turn {turn}: Target's HP = {target.hp}, Kura's mana = {mage.mana}")