import os


def get_size_file():
    files_dict = {}
    size_files = []
    number = 1
    count = 0

    for dir_path, dir_name, file_name in os.walk('../Lazarev_Viktor_dz_7'):
        if file_name:
            for file in file_name:
                size_files.append(os.path.getsize(os.path.join(dir_path, file)))  # Прошёлся и собрал список размеров

    while max(size_files) > number:  # В собраном списке ищу подходящие по условию и считаю
        number *= 10
        for num in size_files:
            if number / 10 < num < number:
                count += 1
        files_dict[number] = count  # Заполняю словарь вычеслинных значений
        count = 0

    for key, value in files_dict.items():  # Для красивого вывода словаря
        print(f'Размер файлов меньше {key} байт = {value}')


get_size_file()
