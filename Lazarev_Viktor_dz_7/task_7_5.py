import os


def get_size_file():
    files_dict = {}
    size_files = []
    number = 1
    count = 0
    extension = []

    for dir_path, dir_name, file_name in os.walk('../Lazarev_Viktor_dz_7'):
        if file_name:
            for file in file_name:
                size_files.append(os.path.getsize(os.path.join(dir_path, file)))  # Прошёлся и собрал список размеров
                size_files.append(file.split('.')[1])  # Добавил расширения файлов

    while max(size_files[::2]) > number:  # Сделал срез чтоб найти максимальное число и пропустить строки
        number *= 10
        for i, num in enumerate(size_files[::2]):  # Прохожусь с помощью среза также по int значениям
            if number / 10 < num < number:
                count += 1
                if not size_files[i * 2 + 1] in extension:  # Проверяю список на наличие расширения и заполняю нужными
                    extension.append(size_files[i * 2 + 1])
            files_dict[number] = count, extension  # Заполняю словарь вычеслинных значений в виде кортежа
        count = 0
        extension = []

    with open('summary.json', 'w', encoding='utf-8') as file:
        for key, value in files_dict.items():                           # Для красивой записи в файл
            file.write(f'Размер файлов меньше {key} байт = {value}\n')


get_size_file()
