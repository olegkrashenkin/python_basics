from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']

a = ((t, k) for t, k in zip_longest(tutors, klasses) if t is not None)

# Доказать, что вы создали именно генератор.
print(type(a))

# Проверить его работу вплоть до истощения.
for i in a:
    print(i)

print(list(a))