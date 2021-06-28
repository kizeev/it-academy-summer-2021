# Языки
# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N. Далее идет N
# чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих строках - список таких
# языков.

# Создать словарь: ключ = номер школьника, значение = список языков
num_schoolboy = input('Введите количество школьников: ')
count1 = 1
dict_schoolboy_lang = {}

while count1 <= int(num_schoolboy):
    num_lang = input(f'Количество языков школьника № {count1}: ')
    set_lang = set()
    count2 = 1
    while count2 <= int(num_lang):
        lang = input('Перечислите языки: ')
        set_lang.add(lang)
        count2 += 1
    dict_schoolboy_lang[count1] = set_lang
    count1 += 1

# Получить языки, которые знает хотя бы один школьник
anyknown_lang = set()
for value in dict_schoolboy_lang.values():
    anyknown_lang.update(value)

# Получить языки, которые знают все школьники
allknown_lang = anyknown_lang.copy()
for value in dict_schoolboy_lang.values():
    allknown_lang.intersection_update(value)

# Выходные данные
print(f'Кол-во языков, которые знают все: {len(allknown_lang)}')
for lang in allknown_lang:
    print(lang)

print(f'Кол-во языков, которые знает хотя бы один: {len(anyknown_lang)}')
for lang in anyknown_lang:
    print(lang)
