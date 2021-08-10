"""Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
"""


class TooManyErrors(Exception):
    """Исключение возбуждается, если превышено количество попыток вызова"""
    def __init__(self, text):
        self.text = text


def number_of_attempts(number):  # декоратор с параметром
    def decorator(func):
        def wrapper(*args):
            count = number
            while count > 0:
                try:
                    func(*args)
                    break
                except ValueError:
                    print('Это не число!!')
                    count -= 1
            else:
                raise TooManyErrors('Превышено количество попыток вызова')
        return wrapper
    return decorator


@number_of_attempts(5)
def square_number():
    """Вычислить квадрат числа"""
    input_number = int(input('Введите число: '))
    print(f'Квадрат вашего числа: {input_number ** 2}')


square_number()
