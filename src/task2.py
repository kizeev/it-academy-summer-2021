""" Создайте декоратор, который хранит результаты вызовов функции (за все время
вызовов, не только текущий запуск программы).
"""


def decorator(func):
    count = []

    def wrapper(*args, **kwargs):
        count.append(1)
        print('количество вызовов: ', count)
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def add_func(x, y):
    print(x + y)


add_func(5, 7)
add_func(2, 4)
