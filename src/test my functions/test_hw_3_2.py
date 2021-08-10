import ddt
from hw_3 import sort_list
import unittest


@ddt.ddt
class TestSortList(unittest.TestCase):
    """Тестирование функции, которая перемещает все ненулевые элементы в

    левую часть списка, не меняя их порядок, а все нули - в правую часть
    """

    @ddt.data(
        ([1, 2, 0, 4, 'f', 0, []], [1, 2, 4, 'f', [], 0, 0]),
        ([], []),
        ([0, 1], [1, 0]),
    )
    @ddt.unpack
    def test_positive(self, input_data, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = sort_list(input_data)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (6, TypeError),
        ({0: 'a', 2: 'b'}, AttributeError),
        ({0, 2}, AttributeError),
    )
    @ddt.unpack
    def test_wrong_data(self, input_data, expected_error):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_error):
            sort_list(input_data)

    def test_right_sort(self):
        """Проверить, чтобы длина входных и выходных данных совпадала"""
        result = sort_list([1, 0, 3, 0, 2])
        self.assertCountEqual(result, [1, 0, 3, 0, 2])


if __name__ == '__main__':
    unittest.main()
