from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as file_user:
    with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
        users = (user.strip() for user in file_user)
        hobbies = (hobby.strip() for hobby in file_hobby)
        users_data = [f'{user} : {hobby}\n' if user else exit('1')
                      for user, hobby in zip_longest(users, hobbies)]

with open('users_hobby.txt', 'w', encoding='utf-8') as file_write:
    file_write.writelines(users_data)
