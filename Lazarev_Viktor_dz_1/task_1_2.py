# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.


cubes = [i ** 3 for i in range(1, 1001, 2)]

total = 0
sum_number = 0

for number in cubes:
    save_number = number
    while number > 0:
        num = number % 10
        sum_number += num
        number //= 10
    if sum_number % 7 == 0:
        total += save_number
    sum_number = 0

print('Сумма чисел: ', total)

for i, j in enumerate(cubes):
    cubes[i] += 17

total_1 = 0
sum_number_1 = 0

for number in cubes:
    save_number = number
    while number > 0:
        num = number % 10
        sum_number_1 += num
        number //= 10
    if sum_number_1 % 7 == 0:
        total_1 += save_number
    sum_number_1 = 0

print('Сумма чисел после +17: ', total_1)
