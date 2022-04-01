import os


def starter(folders):
    if not os.path.exists(folders[0]):
        os.mkdir(folders[0])
        for folder in folders[1:]:
            if not os.path.exists(os.path.join('my_project', folder)):
                os.mkdir(os.path.join('my_project', folder))
            else:
                print(f'Папка {folder} уже существует')
    else:
        print(f'Папка {folders[0]} уже существует')


name_folders = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
starter(name_folders)
