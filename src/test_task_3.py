"""Оформите указанную задачу из прошлых домашних в виде функции и покройте
тестами. Учтите, что в функцию могут быть переданы некорректные значения, здесь
может пригодится ‘assertRaises’. Не нужно переделывать функцию для того чтобы
она ловила все возможные ситуации сама.

Вариант 6
Домашняя 4. Задача 7.
"""


import ddt
import task_3
import unittest


@ddt.ddt
class TestEuclidAlgorithm(unittest.TestCase):
    """Тестирование функции алгоритма Евклида"""

    @ddt.data(
        (1, 4, 1),
        (6, 9, 3),
        (8, 12, 4),
    )
    @ddt.unpack
    def test_right_data(self, input_num1, input_num2, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = task_3.euclid_algorithm(input_num1, input_num2)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ('12', 6, TypeError),
        ([15], 1, TypeError),
        (2, {}, TypeError),
    )
    @ddt.unpack
    def test_wrong_data(self, input_num1, input_num2, expected_result):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_result):
            task_3.euclid_algorithm(input_num1, input_num2)

    @ddt.data(
        (0, 0),
        (0, 1),
        (1, 0),
    )
    @ddt.unpack
    def test_zero(self, input_num1, input_num2):
        """Проверить, чтобы входные данные не были равны 0"""
        result = task_3.euclid_algorithm(input_num1, input_num2)
        self.assertTrue(result <= 1, 'Ноль не имеет делителей!')


if __name__ == '__main__':
    unittest.main()
