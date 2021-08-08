import ddt
from hw_3 import unique_elements
import unittest


@ddt.ddt
class TestUniqueElements(unittest.TestCase):
    """Тестирование функции, которая возвращает уникальные элементы в списке
    в том же порядке
    """

    @ddt.data(
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ('asddf', ['a', 's', 'f']),
        ([1, 'fff', [], 1], ['fff', []]),
    )
    @ddt.unpack
    def test_positive(self, input_data, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = unique_elements(input_data)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (6, TypeError),
        ({1: 'a', 2: 'b'}, AttributeError),
    )
    @ddt.unpack
    def test_wrong_data(self, input_data, expected_result):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_result):
            unique_elements(input_data)

    @ddt.data(
        ([1, 1, 2, 3], 1),
        ('asdd', 'd'),
    )
    @ddt.unpack
    def test_not_in(self, input_data, element):
        """Проверить, чтобы чтобы повторяющийся элемент отсутствовал в итоге"""
        result = unique_elements(input_data)
        self.assertNotIn(element, result)


if __name__ == '__main__':
    unittest.main()
