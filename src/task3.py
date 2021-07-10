""" Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”.
"""

input_list = [2, 3, 8, 9]
edit_list = [str(input_list[0])]

for number in range(1, len(input_list)):

    # Сравнить текущее число с предыдущим и последующим, если да - ничего
    # не делать
    if input_list[number - 1] == input_list[number] - 1 and\
            input_list[number + 1] == input_list[number] + 1:
        pass

    # Сравнить текущее число только с предыдущим, если да - дефис
    elif input_list[number - 1] == input_list[number] - 1:
        edit_list.append('-' + str(input_list[number]) + ',')

    # Сравнить текущее число только с последующим, если да - текущее число
    elif input_list[number + 1] == input_list[number] + 1:
        edit_list.append(str(input_list[number]))
    else:
        edit_list.append(',' + str(input_list[number]) + ',')

edit_list.append(str(input_list[-1]))

print(edit_list)

result_string = ''.join(edit_list)
print(result_string)
