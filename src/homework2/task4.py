inp_str = input("Введите текст: ")

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
inp_str1 = ''
for i in inp_str:
    if i in a:
        inp_str1 += i

low_str = inp_str1.lower()
low_str1 = ''
for i in inp_str1:
    if i not in low_str:
        low_str1 += i
print("Количество прописных букв = " + str(len(low_str1)))

up_str = inp_str1.upper()
up_str1 = ''
for i in inp_str1:
    if i not in up_str:
        up_str1 += i
print("Количество строчных букв = " + str(len(up_str1)))
