def del_spaces(input_text=''):
    """Удалить из строки повторяющиеся символы и все пробелы."""
    input_text = input_text.replace(' ', '')
    new_text = ''

    for item in input_text:
        if item not in new_text:
            new_text = new_text + item

    return new_text


def triangle(a=1, b=1, c=1):
    """Проверить, действительно ли это стороны треугольника."""
    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        square = square ** 0.5
        square = str(square)
        return "Это треугольник площадью " + square[:5]
    else:
        return "Это НЕ треугольник"
