n = int(input("Введите n-е число Фибоначчи: "))

f1 = 0
f2 = 1
i = 1

if i != n:
    while i < n:
        f1, f2 = f2, f1 + f2
        i += 1

print(f1)
