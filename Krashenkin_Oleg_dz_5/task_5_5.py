src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
a = [i for i in src if src.count(i) == 1]
print(a)
# Второй вариант
b = [v for k, v in enumerate(src) if v not in src[:k] and v not in src[:k:-1]]
print(b)
