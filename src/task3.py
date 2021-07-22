""" Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”.
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(input_list):
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

    print(result_string)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
