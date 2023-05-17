with open("test/data/lst_tuples.txt", "r") as file:
    text = file.readlines()

for numbers in text:
    left_operand, right_operand, element = numbers.split()
    if element == "1":
        print(f"{left_operand} + {right_operand} = {int(left_operand) + int(right_operand)}")
    elif element == "2":
        print(f"{left_operand} - {right_operand} = {int(left_operand) - int(right_operand)}")
    elif element == "3":
        print(f"{left_operand} * {right_operand} = {int(left_operand) * int(right_operand)}")
