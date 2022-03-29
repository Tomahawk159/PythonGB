from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as file_user:
    with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
        users = (user.strip().replace(',', '') for user in file_user)
        hobbies = (hobby.strip().replace(',', '') for hobby in file_hobby)
        users_data = {key: value if key else exit('1') for key, value in zip_longest(users, hobbies)}

with open('data_users.csv', 'a', encoding='utf-8') as file:
    for key, value in users_data.items():
        file.write(key + ': ' + str(value) + '\n')
