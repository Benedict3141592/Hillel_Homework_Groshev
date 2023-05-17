import string

# Open file text.txt
with open("D:/Download/text.txt") as file:
    text = file.read()

# Creating dictionary with alphabet and count letters
letters = string.ascii_lowercase
dict_count = {}
text = text.lower()

for letter in letters:
    dict_count[letter] = text.count(letter)

print(dict_count)
