"""Оформите указанную задачу из прошлых домашних в виде функции и покройте
тестами. Учтите, что в функцию могут быть переданы некорректные значения, здесь
может пригодится ‘assertRaises’. Не нужно переделывать функцию для того чтобы
она ловила все возможные ситуации сама.

Вариант 6
Домашняя 4. Задача 7.
"""


def euclid_algorithm(num1=1, num2=2):
    """Числа
    Даны два натуральных числа. Вычислите их наибольший общий делитель при
    помощи алгоритма Евклида (мы не знаем функции и рекурсию).
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 + num2
