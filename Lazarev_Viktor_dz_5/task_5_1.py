def odd_numbers(value):
    for num in range(1, value + 1, 2):
        yield num


number = int(input('Введите число: '))
odd_to_number = odd_numbers(number)
print(*odd_to_number)  # Распаковал и опустошил генератор
print(next(odd_to_number))  # Попытка достать значения StopIteration
