def without_vowels(string: str) -> str:
    return "".join(word for word in string if word not in "aeiou")


print(without_vowels("Hello my name is Siri"))
