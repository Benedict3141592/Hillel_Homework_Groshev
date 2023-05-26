"""
Implement your own implementation of function max and min
"""


def function_max(items: list or tuple, value: int) -> int or list:
    items = sorted(items, reverse=True)
    if value == 1:
        return items[0]
    return items[0:value]


def function_min(items, value):
    items = sorted(items, reverse=False)
    if value == 1:
        return items[0]
    return items[0:value]


if __name__ == "__main__":
    print(function_max((1, 2, 3, 4, 4), value=2))
    print(function_min([1, 2, 3, 4, 1, 22], value=1))
