def convert_line(path: str):
    with open(path, "r") as file:
        text = file.readlines()

    with open(path, "w") as file:
        for line in text:
            converted_line = "".join([word for word in line if word not in "1234567890"])
            file.write(converted_line)


convert_line("../hw6.txt")
