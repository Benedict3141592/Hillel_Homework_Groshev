"""
Implement your own implementation of the function map
"""


def function_map(callback, sequence):
    res = []
    for item in sequence:
        res.append(callback(item))
    return res


print(function_map(lambda x: x ** 2, (1, 2, 3, 4, 5)))
