# Первый вариант. Только для кубов чисел <= 1000.
# Использую функцию только чтобы не копипастить.
# Изменяю список через range(len())
def task_func1(some_list):
    result = 0
    for number in some_list:
        if (
                number // 10 ** 8 + number % 10 ** 8 // 10 ** 7 + number % 10 ** 7 //
                10 ** 6 + number % 10 ** 6 // 10 ** 5 + number % 10 ** 5 //
                10 ** 4 + number % 10 ** 4 // 10 ** 3 + number % 10 ** 3 //
                10 ** 2 + number % 10 ** 2 // 10 + number % 10 // 1) % 7 == 0:
            result += number
    return result


num_list = []
for number_ in range(1, 1001, 2):
    num_list.append(number_ ** 3)
print(task_func1(num_list))
for index in range(len(num_list)):
    num_list[index] += 17
print(task_func1(num_list))


# Последний вариант. Универсальный, но долгий.
# Использую функцию только чтобы не копипастить.
# Изменяю список через enumerate()
def task_func2(some_list):
    result = 0
    for number in some_list:
        numbers = []
        numbers.append(number)
        len_int = 0
        if number == 0:
            len_int += 1
        while number:
            number //= 10
            len_int += 1
        for number in numbers:
            n = 1
            temp_result = 0
            while len_int != 0:
                num_ = number % 10 ** (n + 1) // 10 ** n
                n = n + 1
                len_int -= 1
                temp_result += num_
                if len_int == 0:
                    temp_result += number % 10 // 1
                    if temp_result % 7 == 0:
                        result += number
    return result


num_list = []
for number_ in range(1, 1001, 2):
    num_list.append(number_ ** 3)
print(task_func2(num_list))
for index, val in enumerate(num_list):
    num_list[index] = val + 17
print(task_func2(num_list))
