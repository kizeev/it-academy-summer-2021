# Города
# Дан список стран и городов каждой страны. Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая
# строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия
#  каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный
# город.

# Создать словарь: ключ = страна, значение = список городов
num_country = int(input('Введите количество стран: '))
count1 = 0
dict_country = {}

while count1 < num_country:
    country_city = input('Введите страну и ее города: ')
    dict_country[country_city.split()[0]] = country_city.split()[1:]
    count1 += 1

# Создать список запрашиваемых городов
num_city = int(input('Введите количество запросов: '))
count2 = 0
list_city = []

while count2 < num_city:
    city = input('Введите города: ')
    list_city.append(city)
    count2 += 1

# Проверить по каждому городу вхождение в словарь и вывести название страны
for city in list_city:
    for country in dict_country:
        if city in dict_country.get(country):
            print(country)
