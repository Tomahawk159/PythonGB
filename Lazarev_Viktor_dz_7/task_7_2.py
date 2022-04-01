import yaml
import os

structure = {'my_project': [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'], },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                     ]
         }
    ]
}
with open('config.yaml', 'w', encoding='utf-8') as file:
    file.write(yaml.dump(structure))

with open('config.yaml', 'r', encoding='utf-8') as file_1:
    file_dict = yaml.safe_load(file_1)


def create_folders(data):
    for key, value in data.items():
        if not os.path.exists(key):
            os.mkdir(key)  # Проверяем на наличие папки, создаём
        os.chdir(key)  # Углубляемся
        for val in value:  # Проходимся по значениям
            if isinstance(val, dict):  # Eсли словарь то рекурсивно заходим дальше, иначе создаём файл в папке
                create_folders(val)
            else:
                with open(val, 'w', encoding='utf-8') as w_f:
                    w_f.write('')
    os.chdir('../')  # Выходим выше


create_folders(file_dict)
