def three_in_number(last_number=1000) -> list:
    return [number for number in range(last_number) if "3" in str(number)]


if __name__ == "__main__":
    print(three_in_number())
