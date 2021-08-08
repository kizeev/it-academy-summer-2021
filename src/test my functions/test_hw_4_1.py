import ddt
from hw_4 import cities
import unittest


@ddt.ddt()
class TestCities(unittest.TestCase):
    """Тестирование функции, которая на вход получает строки со странами и их
    городами, а возвращает страну по ее городу
    """

    @ddt.data(
        (1, 'Беларусь Минск Гродно Брест', 1, 'Гродно', 'Беларусь'),
        (1, 'Беларусь Минск Гродно Брест', 1, 'Брест', 'Беларусь'),
        (1, 'Беларусь Минск Гродно Брест', 1, 'Минск', 'Беларусь'),
        (1, 'Беларусь Минск Гродно Брест', 1, 'Гомель', 'Страна неизвестна'),
    )
    @ddt.unpack
    def test_positive(self, inp_num_country, inp_country_city, inp_num_city,
                      inp_city, expected_result):
        """Сравнить результат функции с ожидаемым результатом"""
        result = cities(inp_num_country, inp_country_city, inp_num_city,
                        inp_city)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ('a', 'Беларусь Минск Гродно Брест', 1, 'Гродно', ValueError),
        (1, '', 1, 'Гродно', IndexError),
        (1, 1, 1, 'Гомель', AttributeError),
        (1, ['Беларусь', 'Минск', 'Брест'], 1, 'Брест', AttributeError),
    )
    @ddt.unpack
    def test_wrong_data(self, inp_num_country, inp_country_city, inp_num_city,
                        inp_city, expected_error):
        """Проверить тип входных данных в функцию"""
        with self.assertRaises(expected_error):
            cities(inp_num_country, inp_country_city, inp_num_city,
                   inp_city)


if __name__ == '__main__':
    unittest.main()
