lst = ["FirstItem", "FriendsList", "MyTuple", "Anotherword", "word", "Another_dict"]
res = []

# First option
# for word in lst:
#     word = word.lower()
#     if len(word) <= 4 or "_" in word:
#         res.append(word)
#     elif word[-4:] == "item" or word[-4:] == "list":
#         word = list(word)
#         word.insert(-4, "_")
#         res.append("".join(word))
#     elif word[-5:] == "tuple":
#         word = list(word)
#         word.insert(-5, "_")
#         res.append("".join(word))
#     else:
#         word = list(word)
#         word.insert(-4, "_")
#         res.append("".join(word))

# Second option (optimised)
for word in lst:
    word = word.lower()
    if len(word) <= 4 or "_" in word:
        res.append(word)
    elif word[-5:] == "tuple":
        word = list(word)
        word.insert(-5, "_")
        res.append("".join(word))
    else:
        word = list(word)
        word.insert(-4, "_")
        res.append("".join(word))

print(res)
