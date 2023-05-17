string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
dic_string = {}

string = string.strip()
string = string.split("=")
string = " ".join(string)
string = string.split("&")
string = " ".join(string)
string = string.split(" ")
string.pop(2)
string.pop(4)

for index in range(0, len(string), 2):
    dic_string[string[index]] = string[index + 1]

print(dic_string)
