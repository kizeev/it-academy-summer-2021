""" Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""

list_number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_number2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

result = set(list_number1) & set(list_number2)

print(len(result))
