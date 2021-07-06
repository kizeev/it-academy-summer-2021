""" Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”.
"""

input_list = [0, 1, 2, 4, 7, 8, 10]
edit_list = [str(input_list[0])]

for number in range(1, len(input_list)):
    if input_list[number - 1] == input_list[number] - 1 and\
            input_list[number + 1] == input_list[number] + 1:
        edit_list.append(',')
    elif input_list[number - 1] == input_list[number] - 1:
        edit_list.append('-')
        edit_list.append(str(input_list[number]))
        edit_list.append(',')
    else:
        edit_list.append(str(input_list[number]))
        edit_list.append(',')

print(edit_list)

result_string = ''.join(edit_list)
print(result_string)

