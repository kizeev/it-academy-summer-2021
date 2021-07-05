""" Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”.
"""

input_list = [0, 1, 2, 3, 4, 7, 8, 10]
edit_list = [input_list[0]]

for number in range(1, len(input_list)):
    if edit_list[-1] == input_list[number - 1] and edit_list[-1] != '-':
        edit_list.append('-')
    else:
        edit_list.append(input_list[number])


print(edit_list)
