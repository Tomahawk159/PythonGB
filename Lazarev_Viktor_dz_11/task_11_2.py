class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


number = int(input('Введите число: '))

try:
    if number == 0:
        raise DivisionByZero('На ноль делить нельзя')
except DivisionByZero as error:
    print(error.text)
else:
    print('Введенно коректное значение')
finally:
    print('Программа отработала')
