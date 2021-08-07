def decorator(func):
    """ Создайте декоратор, который хранит результаты вызовов функции (за все
    время вызовов, не только текущий запуск программы).
    """
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


def max_divisor(num):
    """ Вводится число найти его максимальный делитель, являющийся степенью
    двойки.
    10(2) 16(16), 12(4).
    """
    degree = 0
    list_divisors = []

    while num > 2 ** degree:
        degree += 1
        list_divisors.append(2 ** degree)

    list_divisors = sorted(list_divisors, reverse=True)

    for divisor in list_divisors:
        if num % divisor == 0:
            print(divisor)
            break
