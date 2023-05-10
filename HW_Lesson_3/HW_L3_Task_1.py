lst_elements = [1, 2, 3, 4, 5, 6, 7, 8]
lst_odd_index = []
lst_even_index = []

for index, number in enumerate(lst_elements):
    if index % 2 == 0:
        lst_odd_index.append((index, number))
    else:
        lst_even_index.append((index, number))

print(lst_odd_index)
print(lst_even_index)
