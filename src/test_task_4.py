import ddt
from task_4 import various_elements_multi_table
import unittest


@ddt.ddt
class TestVariousElements(unittest.TestCase):
    """Тестирование функции, которая находит различные элементы таблицы
     умножения
     """

    @ddt.data(
        (3, 4, 8),
        (64, 64, 1263),
        (12, 345, 1998),
    )
    @ddt.unpack
    def test_positive(self, input_num1, input_num2, expected_value):
        result = various_elements_multi_table(input_num1, input_num2)
        self.assertEqual(result, expected_value)

    @ddt.data(
        ('a', 4, TypeError),
        ([1], 5, TypeError),
        ((10,), 20, TypeError),
    )
    @ddt.unpack
    def test_wrong_data(self, input_value1, input_value2, expected_error):
        with self.assertRaises(expected_error):
            various_elements_multi_table(input_value1, input_value2)


if __name__ == '__main__':
    unittest.main()
