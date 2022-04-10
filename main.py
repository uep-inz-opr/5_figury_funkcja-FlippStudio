i = input()

f_sum = 0.0


def circle(r):
    from math import pi
    return pi * r ** 2


def rectangle(a, b):
    return a * b


def triangle_heron(a, b, c):
    from math import sqrt

    p = (a + b + c)/2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def figures(num):
    num = [float(n) for n in num]
    n_len = len(num)

    if n_len == 1:
        return circle(num[0])

    elif n_len == 2:
        return rectangle(num[0], num[1])

    elif n_len == 3:
        return triangle_heron(num[0], num[1], num[2])


flag = True

for j in range(int(i)):
    numbers = input()
    l_numbers = numbers.split(' ')
    if len(l_numbers) > 3:
        print("Błąd: można podać maksymalnie 3 liczby")
        flag = False
        break
    temp = figures(l_numbers)
    f_sum += temp

if flag:
    print(round(f_sum, 2))
