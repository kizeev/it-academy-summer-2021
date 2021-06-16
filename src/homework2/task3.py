inp_text = input("Введите текст: ")

inp_text = inp_text.replace(' ', '')
n_text = ''

for i in inp_text:
    if i not in n_text:
        n_text = n_text + i

print(n_text)
