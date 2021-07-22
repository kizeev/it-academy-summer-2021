""" Оформите решение задач из прошлых домашних работ в функции. Напишите
 функцию runner. (все станет проще когда мы изучим модули, getattr и setattr).
 a. runner() – все фукнции вызываются по очереди
 b. runner(‘func_name’) – вызывается только функцию func_name.
 c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

from inspect import getmembers, isfunction
import task1_1

functions_list = getmembers(task1_1, isfunction)


def runner(*args):
    if not args:
        for element in functions_list:
            func = element[1]
            func()
    else:
        for func_name in args:
            for element in functions_list:
                if func_name == element[0]:
                    func = element[1]
                    func()


runner()
runner('total_price')
runner('total_price', 'longest_word', 'languages')
