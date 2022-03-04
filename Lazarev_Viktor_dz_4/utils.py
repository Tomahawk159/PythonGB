import requests
import datetime


def currency_rates(currency):
    file_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    list_data = file_xml.text.split('><')
    date_xml = None

    for i, j in enumerate(list_data):
        if 'Date' in j:
            date_xml = list_data[i][14:24]
            date_xml = datetime.datetime.strptime(date_xml, '%d.%m.%Y')
        if currency.upper() == j[9:-10]:
            value = list_data[i + 3][6:-7]
            return f'{round(float(value.replace(",", ".")), 2)}, {date_xml.date()}'


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))
