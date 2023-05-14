lst = ["FirstItem", "FriendsList", "MyTuple"]
res = []

for word in lst:
    word = word.lower()
    if word[-4:] == "item" or word[-4:] == "list":
        word = list(word)
        word.insert(-4, "_")
        res.append("".join(word))
    elif word[-5:] == "tuple":
        word = list(word)
        word.insert(-5, "_")
        res.append("".join(word))
    else:
        res.append(word)

print(res)
