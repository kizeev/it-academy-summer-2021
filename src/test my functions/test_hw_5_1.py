import ddt
from hw_5 import get_ranges
import unittest


@ddt.ddt
class TestGetRanges(unittest.TestCase):
    """Тестирование функции, которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
    список “сворачивает”
    """

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], '0-4, 7-8, 10'),
        ([4, 7, 10], '4, 7, 10'),
        ([2, 3, 8, 9], '2-3, 8-9'),
    )
    @ddt.unpack
    def test_positive(self, input_data, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = get_ranges(input_data)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ('0, 1, 2, 3, 4, 7, 8, 10', TypeError),
        ([], IndexError),
        ([1], IndexError),
        ({1, 2, 5}, TypeError),
    )
    @ddt.unpack
    def test_wrong_data(self, input_data, expected_error):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_error):
            get_ranges(input_data)


if __name__ == '__main__':
    unittest.main()
