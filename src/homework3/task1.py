# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
# одновременно кратных и 3 и 5 - FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
