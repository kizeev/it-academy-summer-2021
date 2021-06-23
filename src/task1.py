# Dict comprehensions
# Создайте словарь с помощью генератора словарей, так чтобы его ключами были
# числа от 1 до 20, а значениями кубы этих чисел.

dictionary = {}

for i in range(1, 21):
    dictionary[i] = i ** 3

print(dictionary)
