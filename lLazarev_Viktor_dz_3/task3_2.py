# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

translate = {'one':	'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
             'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(number):
    if number.lower() in translate:
        if number == number.capitalize():
            number = number.lower()
            return translate[number].capitalize()
        else:
            return translate[number]
    else:
        return None


print(num_translate('Eight'))
