input_ = int(input("Введите число: "))

a = 0
b = 0
c = input_

while c > 0:
    b = c % 10
    a = a * 10 + b
    c = c // 10

if a == input_:
    print("Это палиндром")
else:
    print("Это НЕ палиндром")
