number_user = int(input('Введите число: '))
numbers_gen = (number for number in range(1, number_user + 1, 2))
print(type(numbers_gen))
print(*numbers_gen)
