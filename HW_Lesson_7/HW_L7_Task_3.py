"""
Implement your own implementation of the function map
"""


def function_map(callback, sequence: list or tuple) -> list:
    res = []
    for item in sequence:
        res.append(callback(item))
    return res


if __name__ == "__main__":
    print(function_map(lambda x: x ** 2, (1, 2, 3, 4, 5)))
