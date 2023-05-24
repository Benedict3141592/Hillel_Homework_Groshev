"""
Write a function that, given a string S denoting the directions of the arrows, returns

the minimum number of arrows that must be rotated to make them all point in the same

direction
"""


def min_numbers_of_arrow(string):
    dict_items = {}
    for item in string:
        dict_items[item] = string.count(item)
    return len(string) - max(dict_items.values())


print(min_numbers_of_arrow("^vv<v"))
print(min_numbers_of_arrow("v>>>vv"))
print(min_numbers_of_arrow("<<<"))
