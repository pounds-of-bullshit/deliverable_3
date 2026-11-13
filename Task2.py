# code for task 2
import random

from dice import Dice

# A demonstration of the Dice class

# Creates a dice with n numbers of sides
d6 = Dice() # 6 sides
d20 = Dice(sides=20) # 20 sides

print(repr(d6))
print(repr(d20))
print(f"Roll using roll(): {d6.roll()}")
print(f"Roll using __call__(): {d20()}")

# Repeated dice rolls
# Sets a seed to repeat the same random results
random.seed(42)

# Generates 10 dice rolls for the six-sided one
rolls = [d6.roll() for _ in range(10)]
print(f"10 d6 rolls: {rolls}")
# The valid results are the ones between 1 and 6
print(f"All rolls are valid: {all(1 <= value <= 6 for value in rolls)}")