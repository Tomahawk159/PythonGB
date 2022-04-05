import re

RE = re.compile(r'((?:[a-z0-9]+(?:(?:[:]|[.]){1,2})){3,7}[a-z0-9]+).{5}\[\d{1,2}\/[a-zA-Z]+\/\d{4}\:\d{2}\:\d{2}\:\d{2}'
                r'.\+\d+\] "[A-Z]+ (\/[a-zA-Z]+){2}\_\d \w{1,4}\/\d[.]\d\" \d+ \d+')  # Регулярка ищет как IPV4 так и IPV6
log_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        pars = RE.match(line)
        value = pars.group().split()  # Создал список
        parsed_raw = value[0], value[3][1:] + ' ' + value[4][:-1], value[5][1:], value[6], value[8], value[9]  #Собрал нужную строку
        log_list.append(parsed_raw)


with open('nginx_logs_write.txt', 'w', encoding='utf-8') as f:
    for log in log_list:
        f.write(str(log) + '\n')
