# Точно по заданию
for percent in range(1, 21):
    if percent == 1:
        print(f'{percent} процент')
    elif 2 <= percent <= 4:
        print(f'{percent} процентa')
    elif 5 <= percent <= 20:
        print(f'{percent} процентов')

# Для любого числа
per = input('Введите процент: ')
a = list(per)
if len(a) == 1 and a[-1] == '1' or len(a) > 1 and a[-1] == '1' and a[-2] != '1':
    print(f'{per} процент')
elif len(a) == 1 and a[-1] == '2' or len(a) > 1 and a[-1] == '2' and a[-2] != '1':
    print(f'{per} процента')
elif len(a) == 1 and a[-1] == '3' or len(a) > 1 and a[-1] == '3' and a[-2] != '1':
    print(f'{per} процента')
elif len(a) == 1 and a[-1] == '4' or len(a) > 1 and a[-1] == '4' and a[-2] != '1':
    print(f'{per} процента')
else:
    print(f'{per} процентов')