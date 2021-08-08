import ddt
from hw_5 import max_divisor
import unittest


@ddt.ddt
class TestMaxDivisor(unittest.TestCase):
    """Тестирование функции, которая находит максимальный делитель числа,
    являющийся степень двойки
    """

    @ddt.data(
        (10, 2),
        (16, 16),
        (12, 4),
        (24.0, 8)
    )
    @ddt.unpack
    def test_positive(self, input_data, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = max_divisor(input_data)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ('4', TypeError),
        ([4], TypeError)
    )
    @ddt.unpack
    def test_wrong_data(self, input_data, expected_error):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_error):
            max_divisor(input_data)

    @ddt.data(
        (-2,),
        (0,),
        (1,),
    )
    @ddt.unpack
    def test_is_none(self, input_data):
        """Проверить, вернет ли функция None, если на вход давать числа
        меньше 2
        """
        result = max_divisor(input_data)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
