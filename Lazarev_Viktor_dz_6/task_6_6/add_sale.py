import sys


def add_sale(argv):
    program, number = argv
    with open('../bakery.csv', 'a', encoding='utf-8') as file:
        file.write(str(number) + '\n')


if __name__ == '__main__':
    add_sale(sys.argv)
