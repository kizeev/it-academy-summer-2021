import ddt
from hw_4 import different_words
import unittest


@ddt.ddt()
class TestDiffWords(unittest.TestCase):
    """Тестирование функции, которая считает различные слова в тексте"""

    @ddt.data(
        ('Hello, world', 'В строке встречается 2 различных слов'),
        ('Hello! How are you?', 'В строке встречается 4 различных слов'),
        ('', 'В строке встречается 0 различных слов')
    )
    @ddt.unpack
    def test_positive(self, input_data, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = different_words(input_data)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (1, TypeError),
        ({1: 'hello'}, TypeError),
    )
    @ddt.unpack
    def test_wrong_data(self, input_data, expected_error):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_error):
            different_words(input_data)


if __name__ == '__main__':
    unittest.main()
