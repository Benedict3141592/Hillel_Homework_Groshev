lst_elements = [1, 2, 3, 4, 5, 6, 7, 8]
lst_odd_index = []
lst_even_index = []

for numbers in lst_elements:
    if lst_elements.index(numbers) % 2 == 0:
        lst_odd_index.append((lst_elements.index(numbers), numbers))
    else:
        lst_even_index.append((lst_elements.index(numbers), numbers))

print(lst_odd_index)
print(lst_even_index)
