# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
# одновременно кратных и 3 и 5 - FizzBuzz

lst = []

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        lst.append("FizzBuzz")
    elif i % 5 == 0:
        lst.append("Buzz")
    elif i % 3 == 0:
        lst.append("Fizz")
    else:
        lst.append(i)

print(lst)
