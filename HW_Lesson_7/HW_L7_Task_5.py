"""
Implement your own all function
"""


def function_all(items: list or tuple) -> bool:
    for item in items:
        if not item:
            return False
    return True


if __name__ == "__main__":
    print(function_all((1, 2, 3)))
    print(function_all([1, 2, 3]))
