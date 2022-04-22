import sys


def change_file(argv):
    program, number, new_entry = argv
    lines = []
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        for count, entry in enumerate(file, start=1):
            if count == int(number):
                lines.append(new_entry + '\n')
            else:
                lines.append(entry)
    if count < int(number):
        print('Введено не существующее значение')
    else:
        with open('bakery.csv', 'w', encoding='utf-8') as file:
            file.writelines(lines)


if __name__ == '__main__':
    change_file(sys.argv)
