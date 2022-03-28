# Dice Rolling Simulator

import random

no_of_die = int(input("Number of die you want to roll? "))
count_rolls = 0

while count_rolls < no_of_die:
    print(random.randint(1, 6))
    count_rolls += 1
