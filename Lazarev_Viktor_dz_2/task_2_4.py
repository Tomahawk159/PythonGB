# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
#    (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
#    получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

# B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
#    сортировки остался тот же).

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.

# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_product = [55.8, 46.51, 97, 189.2, 45, 67, 88.0, 21, 39]

total_string = ''

for i in price_product:
    if isinstance(i, float):
        price = str(i).split('.')
        if len(price[1]) < 2:
            price[1] = price[1] + '0'
        total_string += f'{price[0]} руб {price[1]} коп, '
    else:
        total_string += f'{str(i)} руб 00 коп, '

print('Вывод в строку:', total_string[:-2])

print('id До сортировки: ', id(price_product), '\n')

price_product.sort()
print(price_product)
print('id после сортировки: ', id(price_product), '\n')

new_list = sorted(price_product, reverse=True)
print('Отсортирован по убыванию;', new_list)
print('id после сортировки:', id(new_list), '\n')

count = 0
max_price = []
while count != 5:
    count += 1
    max_price.append(max(price_product))
    price_product.remove(max(price_product))

max_price.sort()
print('Отсортированный список 5-ти максимальных цен:', max_price)
