import re

DATE_INT = re.compile(r'\d{1,4}')


class Date:
    def __init__(self, dates):
        self.dates = dates

    @classmethod
    def convert_in_int(cls, param):
        numbers = []
        date_number = DATE_INT.findall(param)  # При помощи регулярки извлекаю числа даты
        for number in date_number:
            number = int(number)
            numbers.append(number)  # Привожу к int заполняю список
        return numbers

    @staticmethod
    def validity_check(date):
        numbers = DATE_INT.findall(date)
        print(numbers)
        if len(numbers) < 3 or int(numbers[0]) not in range(1, 32) or \
                int(numbers[1]) not in range(1, 13) or len(numbers[2]) not in range(1, 5):
            raise ValueError('Некорректная дата')
        else:
            return 'Ok'


print(Date.convert_in_int('02-03-2022'))

print(Date.validity_check('03-03-2022'))
