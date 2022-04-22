import os
import shutil


def creating_folder_templates():
    root_folder = 'my_project'
    template_folder = 'templates'

    if not os.path.exists(os.path.join(root_folder, template_folder)):
        os.mkdir(os.path.join(root_folder, template_folder))  # Проверяем и создаём папку templates

    for dir_path, dir_name, file_name in os.walk(root_folder):  # Ищем html файлы
        if file_name and '.html' in file_name[0]:
            name_folder = dir_path.split('\\')[-1]  # Достаём название папки в котрой хранились шаблоны
            print(name_folder)
            if not os.path.exists(os.path.join(root_folder, template_folder, name_folder)):  # Переносим в templates
                shutil.copytree(dir_path, os.path.join(root_folder, template_folder, name_folder))


creating_folder_templates()
