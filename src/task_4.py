"""Проект Эйлера. Задача 466. Различные элементы таблицы умножения.

Пусть P(m,n) будет количеством различных элементов в таблице умножения m×n.
Например, таблица умножения 3×4 выглядит следующим образом:

×	1	2	3	4
1	1	2	3	4
2	2	4	6	8
3	3	6	9	12

В ней 8 различных элементов {1,2,3,4,6,8,9,12}, поэтому P(3,4) = 8.

Известно, что:
P(64,64) = 1263,
P(12,345) = 1998 и
P(32,10**15) = 13826382602124302.

Найдите P(64,10**16).
"""


from functools import lru_cache
import numpy


@lru_cache(1)
def various_elements_multi_table(m, n):
    various_elements = set()
    for row in range(1, m + 1):
        for column in range(1, n + 1):
            various_elements.add(row * column)
    print(len(various_elements))


def various_elements_multi_table1(m, n):
    count = 0
    if m > n:
        max_num = m
        min_num = n
    else:
        max_num = n
        min_num = m

    for a in range(max_num + 1, m * n + 1):
        # print(a, count)
        for b in range(2, min_num + 1):
            if a % b == 0:
                if a / b <= max_num:
                    count += 1
                    break
    print(max_num + count)


def various_elements_multi_table2(m, n):
    if m >= n:
        max_num = m
        min_num = n
    else:
        max_num = n
        min_num = m

    start_row = 3
    start_column_for_second_row = max_num // 2 + 1

    count = max_num + start_column_for_second_row

    for row in range(3, min_num + 1):
        start_column = max_num // row
        current_row = row
        for num_in_column in range(start_column, max_num + 1):

            current_number = num_in_column * row
            if current_number > max_num:
                if current_number % (current_row - 1) == 0:
                    if current_number / (current_row - 1) <= max_num:
                        continue
                    else:
                        count += 1
                else:
                    if current_row <= 3:
                        count += 1
                    else:
                        current_row -= 1

    print(count)



m, n = 32, 10 ** 7
# various_elements_multi_table(m, n)
various_elements_multi_table2(m, n)

