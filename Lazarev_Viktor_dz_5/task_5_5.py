src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [number for number in src if number not in src[src.index(number)+1:]]
print(result)
