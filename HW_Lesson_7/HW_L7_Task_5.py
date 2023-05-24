"""
Implement your own all function
"""


def function_all(items):
    for item in items:
        if not item:
            return False
    return True


print(function_all([1, 2, 3]))
