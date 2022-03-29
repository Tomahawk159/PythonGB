data_dict = {}

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        ip = line.strip().split()[0]  # Создал список IP
        if ip in data_dict.keys():  # Из списка создал словарь ключ IP значение кол_во обращений
            data_dict[ip] += 1
        else:
            data_dict[ip] = 1

max_spam = (max(data_dict.values()))

for key, value in data_dict.items():
    if value == max_spam:
        print(f'Спамер {key}, обращений {max_spam} раз.')
