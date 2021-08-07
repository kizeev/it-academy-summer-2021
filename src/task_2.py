"""Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
"""


class TooManyErrors(Exception):
    def __init__(self, text):
        self.text = text


def number_of_attempts(number):
    def decorator(func):
        def wrapper(*args):
            count = number
            while count >= 0:
                if count == 0:
                    raise TooManyErrors('Слишком много ошибок!!!')
                else:
                    try:
                        func(*args)
                        break
                    except ValueError:
                        print('Это не число!!')
                        count -= 1
        return wrapper
    return decorator


@number_of_attempts(5)
def square_number():
    """Вычислить квадрат числа"""
    input_number = int(input('Введите число: '))
    print(f'Квадрат вашего числа: {input_number ** 2}')


square_number()
