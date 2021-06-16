text = input("Введите текст: ")
punct = ',.:;-_!?'

for i in text:
    if i in punct:
        text = text.replace(i, '')

text1 = text.split()
max_text = ''
for i in text1:
    if len(i) > len(max_text):
        max_text = i

print(max_text)
