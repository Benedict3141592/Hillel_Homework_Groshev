import random
import os

# Creating a list of tuples
lst_tuples = []

for number in range(0, 100):
    left_operand = random.randrange(1, 501)
    right_operand = random.randrange(1, 501)
    element = random.randrange(1, 4)
    lst_tuples.append((left_operand, right_operand, element))

# Creating file
os.makedirs("test/data")
with open("test/data/lst_tuples.txt", "w") as file:
    for tuples in lst_tuples:
        file.write(f"{tuples[0]} {tuples[1]} {tuples[2]}\n")
