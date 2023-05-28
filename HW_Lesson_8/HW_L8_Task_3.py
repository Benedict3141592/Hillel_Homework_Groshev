def divisible_by_7(last_number=1000) -> list:
    return [number for number in range(last_number) if number % 7 == 0]


if __name__ == "__main__":
    print(divisible_by_7())