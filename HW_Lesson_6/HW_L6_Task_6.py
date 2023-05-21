def without_vowels(string: str) -> str:
    return "".join(word for word in string if word not in "aeiouAEIOU")


print(without_vowels("HEllo my name is Siri"))
