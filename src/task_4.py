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


def various_elements_multi_table(m, n):
    """Функция находит  различные элементы в таблице умножения путем анализа
    каждого произведения чисел и простого счетчика.

    К сожалению не смог найти более быстрый вариант, хоть и потратил на это
    несколько дней. В интернете есть только одно решение этой задачи, и то на
    С++. Зато сравнил языки и в очередной раз убедился, что python лучше)
    """
    if m >= n:
        max_number = m
        min_number = n
    else:
        max_number = n
        min_number = m

    if max_number % 2 == 0:
        start_column_for_second_row = max_number // 2
    else:
        start_column_for_second_row = max_number // 2 + 1

    count = max_number + start_column_for_second_row

    for number_row in range(3, min_number + 1):
        print(number_row, count)
        start_column = max_number // number_row
        for number_column in range(start_column, max_number + 1):
            current_number = number_column * number_row
            if current_number > max_number:
                for current_row in range(number_row - 1, 0, -1):
                    if current_number % current_row == 0:
                        if current_number / current_row <= max_number:
                            break
                        else:
                            count += 1
                            break
                    else:
                        if number_row <= 3:
                            count += 1
                            break

    print(count)


# various_elements_multi_table(64, 64)  # 1263
# various_elements_multi_table(12, 345)  # 1998
various_elements_multi_table(32, 10**15)  # 13826382602124302
