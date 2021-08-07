import ddt
from hw_2 import del_spaces
import unittest


@ddt.ddt
class TestDelSpaces(unittest.TestCase):
    """Тестирование функции, которая удаляет из строки повторяющиеся символы и
    все пробелы
    """
    @ddt.data(
        ('Hello, world', 'Helo,wrd'),
        ('112233', '123'),
        ('', '')
    )
    @ddt.unpack
    def test_positive(self, input_data, expected_result):
        result = del_spaces(input_data)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (1122, AttributeError),
        (['aabbcc'], AttributeError),
        ({}, AttributeError)
    )
    @ddt.unpack
    def test_wrong_data(self, input_data, expected_error):
        with self.assertRaises(expected_error):
            del_spaces(input_data)


if __name__ == '__main__':
    unittest.main()
