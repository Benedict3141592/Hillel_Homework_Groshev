def is_prime(number: int) -> bool or str:
    if number < 2 or number > 1000:
        return "Number must be from 2 to 1000"
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


print(is_prime(2))
