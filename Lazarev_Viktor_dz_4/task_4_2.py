import requests


def currency_rates(currency):
    file_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    list_data = file_xml.text.split('><')  # сделал из строки список, чтоб пройтись enumerate

    for i, j in enumerate(list_data):
        if currency.upper() == j[9:-10]:  # зная размер строки сделал срез до размера нашего аргумента
            value = list_data[i + 3][6:-7]  # если нашёл в строке,то по [i] обрезаю строку до размера значения
            return f'{round(float(value.replace(",", ".")), 2)}'  # перевожу в float, округляю до 2 и возвращаю строку


print(currency_rates('USd'))
print(currency_rates('EUR'))
