""" Написать программу которая находит ближайшую степень двойки к введенному
числу. 10(8), 20(16), 1(1), 13(16)
"""


def nearest_degree_of_two(num):
    degree = 0
    while num > 2 ** degree:
        degree += 1

    if num - 2 ** (degree - 1) < 2 ** degree - num:
        print(2 ** (degree - 1))
    else:
        print(2 ** degree)


nearest_degree_of_two(10)
nearest_degree_of_two(20)
nearest_degree_of_two(1)
nearest_degree_of_two(13)
