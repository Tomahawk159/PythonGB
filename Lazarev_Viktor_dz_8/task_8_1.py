import re

PATTERN = re.compile(r'^[a-z0-9]+\@[a-z0-9]+\.[a-z]{2}$')
DATA_USER = re.compile(r'[a-z0-9]+')


def email_parse(email):
    data_dict = {}
    if PATTERN.match(email):
        data_user = DATA_USER.findall(email)
        data_dict['user_name'] = data_user[0]
        data_dict['domain'] = data_user[1]
        print(data_dict)
    else:
        raise ValueError('Некорретный email')


email_parse('someone@geekbrains.ru')
