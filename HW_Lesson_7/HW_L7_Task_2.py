"""
Implement your realization of the function filter
"""


def function_filter(callback, sequence: list or tuple) -> list:
    res = []
    for item in sequence:
        if callback(item):
            res.append(item)
    return res


if __name__ == "__main__":
    print(function_filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5]))
