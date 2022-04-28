class NotNumber(Exception):
    def __init__(self, text):
        self.text = text


numbers = []

while True:
    user = input('Введите число: ')
    if user.lower() == 'stop':
        print(numbers)
        break
    else:
        try:
            if user.isdigit():
                numbers.append(int(user))
            else:
                raise NotNumber('Введено не число, введите снова')
        except NotNumber as error:
            print(error)
        finally:
            continue
