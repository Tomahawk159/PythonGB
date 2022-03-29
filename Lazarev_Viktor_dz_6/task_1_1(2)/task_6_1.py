data_list = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        var = line.strip().split()
        data_list.append((var[0], var[5], var[6]))

print(data_list[:3])  # Сделал срез для наглядности, чтоб всю кучу значений не выводить.
