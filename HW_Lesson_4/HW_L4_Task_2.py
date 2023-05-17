lst = ["FirstItem", "FriendsList", "My_Tuple", "AnotherWord_FromougterScope", "word", "Another_Dict", "MyLs"]
res = []
res_word = []

for word in lst:
    if word.islower():
        res.append(word)
    else:
        word_lst = list(word)
        res_word.append(word_lst[0])
        for index in range(1, len(word_lst)):
            if word_lst[index].istitle() and word_lst[index - 1] != "_":
                res_word.append("_")
                res_word.append(word_lst[index])
            else:
                res_word.append(word_lst[index])
    if res_word:
        res.append("".join(res_word))
        res_word.clear()

print(res)
