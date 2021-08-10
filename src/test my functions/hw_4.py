def cities(num_country=1, country_city='Беларусь Минск', num_city=1,
           city='Минск'):
    """Города.

    Дан список стран и городов каждой страны. Затем даны названия городов. Для
    каждого города укажите, в какой стране он находится.
    Входные данные
    Программа получает на вход количество стран N. Далее идет N строк, каждая
    строка начинается с названия страны, затем идут названия городов этой
    страны.В следующей строке записано число M, далее идут M запросов —
    названия каких-то M городов, перечисленных выше.
    Выходные данные
    Для каждого из запроса выведите название страны, в котором находится
    данный город.
    """
    # Создать словарь: ключ = страна, значение = список городов
    count1 = 1
    dict_country = {}

    while count1 <= int(num_country):
        dict_country[country_city.split()[0]] = country_city.split()[1:]
        count1 += 1

    # Создать список запрашиваемых городов
    count2 = 1
    list_city = []

    while count2 <= int(num_city):
        list_city.append(city)
        count2 += 1

    # Проверить по каждому городу вхождение в словарь и вывести название страны
    for city in list_city:
        for country in dict_country:
            if city in dict_country.get(country):
                return country
            else:
                return 'Страна неизвестна'


def different_words(input_string='Hello!     How are you?\n'
                                 ' Where are you going?'):
    """Слова.
    
    Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или большим
    числом пробелов или символами конца строки. Определите, сколько различных
    слов содержится в этом тексте.
    """

    punctuation = '!()-[]{};?:,.;_'
    edit_string = ''

    for element in input_string:
        if element in punctuation:
            edit_string = input_string.replace(element, '')

    words = set(edit_string.split())

    return f'В строке встречается {len(words)} различных слов'
