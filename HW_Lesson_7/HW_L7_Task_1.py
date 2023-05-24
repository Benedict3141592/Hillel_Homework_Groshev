import sys

"""
Implement your own print function. It should work on all operating systems. You can't use build-in print function
"""


def print_func(*args):
    return sys.stdout.write(f"{str(*args)}\n")


print_func("Hello world!")
print_func(1)
print_func("")
print_func()
