import requests
import datetime


def currency_rates(argv):
    program, currency = argv
    file_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    list_data = file_xml.text.split('><')
    date_xml = file_xml.headers['Date'][5:16].replace('-', ' ')
    date_obj = datetime.datetime.strptime(date_xml, '%d %b %Y')

    for i, j in enumerate(list_data):
        if currency.upper() == j[9:-10]:
            value = list_data[i + 3][6:-7]
            return f'{round(float(value.replace(",", ".")), 2)}, {date_obj.date()}'


if __name__ == '__main__':
    import sys
    print(currency_rates(sys.argv))
