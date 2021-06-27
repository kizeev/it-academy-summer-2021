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
# num_schoolboy = int(input('Введите количество школьников: '))
# count1 = 1
# dict_schoolboy_lang = {}
#
# while count1 <= num_schoolboy:
#     num_lang = int(input('Количество языков школьника №' + str(count1) + ': '))
#     set_lang = set()
#     count2 = 1
#     while count2 <= num_lang:
#         lang = input('Перечислите языки: ')
#         set_lang.add(lang)
#         count2 += 1
#     dict_schoolboy_lang[count1] = set_lang
#     count1 += 1

dict_schoolboy_lang = {1: {'bel', 'rus'}, 2: {'eng', 'rus'}, 3: {'fre', 'esp', 'rus'}}
print(dict_schoolboy_lang)

all_lang = set()
allknown_lang = set()
for value in dict_schoolboy_lang.values():
    all_lang |= value
    allknown_lang = all_lang ^ value
print('Количество языков, которые знают все: ' + str(allknown_lang))

# for lang in all_lang:
#     print(lang)

# allknown_lang = set()
# for value in dict_schoolboy_lang.values():
#     allknown_lang |= value
# print('Количество языков, которые знают все: ' + str(len(allknown_lang)))