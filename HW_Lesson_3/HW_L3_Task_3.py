friends_lst = ["John", "Marta", "James"]
enemies_lst = ["John", "Johnatan", "Artur"]

for name in friends_lst:
    if name == "James":
        continue
    elif name not in enemies_lst:
        print(f"{name} we are the best friends")
    else:
        print(f"{name} we are not friends anymore")
