from sys import argv

# Например ../python3 task_6_5.py users.csv hobby.csv result.csv
name, first_file, second_file, result_file = argv


def hobby_funk(first_file, second_file, result_file):
    users = open(f'{first_file}', 'r', encoding='utf-8')
    hobby = open(f'{second_file}', 'r', encoding='utf-8')
    users_hobby = open(f'{result_file}', 'w', encoding='utf-8')
    if len(hobby.readlines()) > len(users.readlines()):
        exit(1)
    users.seek(0)
    hobby.seek(0)
    for lines_users in users:
        users_tmp = lines_users.replace('\n', '')
        for lines_hobby in hobby:
            hobby_tmp = lines_hobby.replace('\n', '')
            break
        if hobby_tmp is not None:
            users_hobby.write(f'{users_tmp}: {hobby_tmp}\n')
            hobby_tmp = None
        else:
            users_hobby.write(f'{users_tmp}: {hobby_tmp}\n')
    users.close()
    hobby.close()
    users_hobby.close()


hobby_funk(first_file, second_file, result_file)
