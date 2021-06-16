# Не записал оригинальное условие
# Задача: из введенных цифр составить максимальное число

def descending_order(num):
    n = []
    for i in str(num):
        n.append(i)
    n.sort(reverse=True)
    n = ''.join(n)
    return int(n)
