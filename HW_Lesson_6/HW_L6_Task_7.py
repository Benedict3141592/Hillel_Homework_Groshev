def display_box(width: int, height: int, character: str) -> str:
    res = []

    for index in range(height):
        if index == 0 or index == height - 1:
            res.append(f"{width * character}\n")
        else:
            res.append(f"{character}{(width - 2) * ' '}{character}\n")

    return "".join(res)


print(display_box(10, 10, "X"))
