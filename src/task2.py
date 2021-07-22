""" Создайте декоратор, который хранит результаты вызовов функции (за все время
вызовов, не только текущий запуск программы).
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        with open('count_func.txt', 'r') as count_func_file:
            count = int(count_func_file.readlines()[-1])
        count_func_file.close()
        result = func(*args, **kwargs)
        next_count = count + 1
        with open('count_func.txt', 'a') as count_func_file:
            count_func_file.write('\n' + str(next_count))
        count_func_file.close()
        return result

    return wrapper


@decorator
def add_func(x, y):
    print(x + y)


add_func(5, 7)
add_func(2, 4)
