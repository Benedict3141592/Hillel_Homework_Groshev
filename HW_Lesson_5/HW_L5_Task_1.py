import random

lst_tuple = []

for number in range(0, 100):
    left_operand = random.randrange(1, 501)
    right_operand = random.randrange(1, 501)
    element = random.randrange(1, 4)
    lst_tuple.append((left_operand, right_operand, element))
print(lst_tuple)