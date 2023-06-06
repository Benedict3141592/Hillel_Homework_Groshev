def freezing(numbers: int):
    res = (number ** 2 for number in range(0, numbers, 2))
    return res


# item = freezing(100)
# for number in item:
#     print(number)


if __name__ == "__main__":
    freezing(1000000000)
