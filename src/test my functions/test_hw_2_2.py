import ddt
from hw_2 import triangle
import unittest


@ddt.ddt
class TestTriangle(unittest.TestCase):
    """Тестирование функции, которая проверяет действительно ли это стороны

    треугольника, если да - то выводит его площадь
    """

    @ddt.data(
        (1, 1, 1, 'Это треугольник площадью 0.433'),
        (3, 4, 5.0, 'Это треугольник площадью 6.0'),
        (1, 2, 3, 'Это НЕ треугольник'),
        (0, 0, 0, 'Это НЕ треугольник'),

    )
    @ddt.unpack
    def test_positive(self, inp_data1, inp_data2, inp_data3, exp_result):
        result = triangle(inp_data1, inp_data2, inp_data3)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ('1', [1], 1, TypeError),
        ({}, 2, 5, TypeError),
    )
    @ddt.unpack
    def test_wrong_data(self, inp_data1, inp_data2, inp_data3, exp_error):
        with self.assertRaises(exp_error):
            triangle(inp_data1, inp_data2, inp_data3)


if __name__ == '__main__':
    unittest.main()
