def func_name_decorator(func):
    def inner(*args, **kwargs):
        print(func.__name__)
        return f"Result = {func(*args, **kwargs)}"

    return inner


@func_name_decorator
def addition(first_number: int, second_number: int) -> int:
    return first_number + second_number


@func_name_decorator
def multiply(first_number: int, second_number: int) -> int:
    return first_number * second_number


if __name__ == "__main__":
    print(addition(22, 33))
    print(multiply(11, 2))
