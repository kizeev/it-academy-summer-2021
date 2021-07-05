""" Слова
 Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
"""

input_sting = 'Hello!     How are you?\n Where are you going?'
punctuation = '!()-[]{};?:,.;_'
edit_string = ''

for element in input_sting:
    if element in punctuation:
        edit_string = input_sting.replace(element, '')

words = set(edit_string.split())

print(f'В строке встречается {len(words)} различных слов')
