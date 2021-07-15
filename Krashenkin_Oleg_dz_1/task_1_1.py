duration = int(input('Введите секунды: '))
dur_list = [86400, 3600, 60, 1]
result_list = []
for i in dur_list:
    if duration < i:
        result_list.append(0)
    else:
        result_list.append(duration // i)
        duration -= result_list[-1] * i
print(f'{result_list[0]} дн {result_list[1]} час {result_list[2]} мин {result_list[3]} сек')


