src = [300, 2, 12, 44, 1, 4, 10, 7, 1, 78, 123, 55]

list_number = [number for number in (src[1:]) if number > src[src.index(number) - 1]]
print(list_number)
