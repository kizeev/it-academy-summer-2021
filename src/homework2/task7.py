a = int(input("Введите 1-ую сторону: "))
b = int(input("Введите 2-ую сторону: "))
c = int(input("Введите 3-ую сторону: "))

if (a + b) > c and (b + c) > a and (c + a) > b:
    p = (a + b + c) / 2
    square = p * (p - a) * (p - b) * (p - c)
    square = square ** 0.5
    square = str(square)
    print("Это треугольник площадью " + square[:5])
else:
    print("Это НЕ треугольник")
