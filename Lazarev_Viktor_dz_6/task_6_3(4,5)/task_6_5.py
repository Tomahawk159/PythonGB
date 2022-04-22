from itertools import zip_longest


def work_file(argv):
    program, name_file_1, name_file_2, name_file_3 = argv

    with open(name_file_1, 'r', encoding='utf-8') as file_user:
        with open(name_file_2, 'r', encoding='utf-8') as file_hobby:
            users = (user.strip() for user in file_user)
            hobbies = (hobby.strip() for hobby in file_hobby)
            users_data = [f'{user} : {hobby}\n' if user else exit('1')
                          for user, hobby in zip_longest(users, hobbies)]
    with open(name_file_3, 'w', encoding='utf-8') as file_write:
        file_write.writelines(users_data)


if __name__ == '__main__':
    import sys
    work_file(sys.argv)
