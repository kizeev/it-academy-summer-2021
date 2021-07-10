""" Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def max_divisor(num):
    degree = 0
    list_divisors = []

    while num > 2 ** degree:
        degree += 1
        list_divisors.append(2 ** degree)

    list_divisors = sorted(list_divisors, reverse=True)

    for divisor in list_divisors:
        if num % divisor == 0:
            print(divisor)
            break


max_divisor(10)
max_divisor(16)
max_divisor(12)
