def get_ranges(input_list):
    """ Реализовать функцию get_ranges.

    Функция получает на вход непустой список неповторяющихся целых чисел,
    отсортированных по возрастанию, которая этот список “сворачивает”.
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
    """

    result_string = str(input_list[0])  # начать строку

    for element in range(1, len(input_list) - 1):
        if input_list[element] - 1 == input_list[element - 1] and\
                input_list[element] + 1 == input_list[element + 1]:
            pass
        elif input_list[element] - 1 == input_list[element - 1]:
            result_string += '-' + str(input_list[element])
        elif input_list[element] + 1 == input_list[element + 1]:
            result_string += ', ' + str(input_list[element])
        else:
            result_string += ', ' + str(input_list[element])

    # завершить строку
    if input_list[-2] + 1 == input_list[-1]:
        result_string += '-' + str(input_list[-1])
    else:
        result_string += ', ' + str(input_list[-1])

    return result_string


def max_divisor(num):
    """ Максимальный делитель.

    Вводится число. найти его максимальный делитель, являющийся степенью
    двойки.
    10(2) 16(16), 12(4).
    """
    degree = 0
    list_divisors = []

    while num > 2 ** degree:
        degree += 1
        list_divisors.append(2 ** degree)

    list_divisors = sorted(list_divisors, reverse=True)

    for divisor in list_divisors:
        if num % divisor == 0:
            return divisor
