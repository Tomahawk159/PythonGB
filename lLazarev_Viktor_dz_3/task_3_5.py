# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


from random import choice, shuffle


def get_jokes(number_jokes, flag=False):
    """
    Функция для генерации словосочетаний
    :param flag: bool
    :param number_jokes: int
    :return: list
    """

    list_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    count = 0

    if flag:
        total = list(zip(nouns, adverbs, adjectives))
        return list(map(' '.join, total))[:number_jokes]
    else:
        while count != number_jokes:
            count += 1
            joke = choice(nouns), choice(adverbs), choice(adjectives)
            list_jokes.append(' '.join(joke))
        return list_jokes


result = get_jokes(5, True)
print(result)
