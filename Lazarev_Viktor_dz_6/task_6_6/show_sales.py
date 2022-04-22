import sys


def show_sales(argv):
    number_stop = None
    number_start = None

    if len(argv) == 2:  # Проверил сколько аргументов испоьзуется, для дальнейшего построения логики
        program, number_start = argv
    elif len(argv) == 3:
        program, number_start, number_stop = argv

    with open('../bakery.csv', 'r', encoding='utf-8') as file:
        for count, line in enumerate(file):
            if number_stop:
                if int(number_start) <= count <= int(number_stop):  # Выводим значения пока счётчик в диапазоне
                    print(line.strip())                             # от заданных значений
            elif number_start:
                if int(number_start) <= count:
                    print(line.strip())
            else:
                print(line.strip())


if __name__ == '__main__':
    show_sales(sys.argv)
