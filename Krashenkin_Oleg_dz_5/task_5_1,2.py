# 1
def odd_num1(n):
    for i in range(1, n + 1, 2):
        yield i


for i in odd_num1(15):
    print(i)


# 2
def odd_num2(n):
    return (i for i in range(1, n + 1, 2))


print(*odd_num2(15))
