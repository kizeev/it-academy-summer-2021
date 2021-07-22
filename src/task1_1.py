""" Оформите решение задач из прошлых домашних работ в функции. Напишите
 функцию runner. (все станет проще когда мы изучим модули, getattr и setattr).
 a. runner() – все фукнции вызываются по очереди
 b. runner(‘func_name’) – вызывается только функцию func_name.
 c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

from string import ascii_letters


def total_price(rub=0, penny=0, amount=0):
    """Посчитать общую цену в рублях и копейках за n товаров."""
    price_amount = (rub * 100 + penny) * amount
    price_rub = price_amount // 100
    price_penny = price_amount % 100
    print(f'Общ. ст-ть: {price_rub} руб. {price_penny} коп.')


def longest_word(text=''):
    """Найти самое длинное слово в введенном предложении."""
    punctuation = ',.:;-_!?'

    for char in text:
        if char in punctuation:
            text = text.replace(char, '')

    text1 = text.split()
    max_text = ''
    for char in text1:
        if len(char) > len(max_text):
            max_text = char

    print(max_text)


def del_spaces(input_text=''):
    """Удалить из строки повторяющиеся символы и все пробелы."""
    input_text = input_text.replace(' ', '')
    n_text = ''

    for item in input_text:
        if item not in n_text:
            n_text = n_text + item

    print(n_text)


def lower_upper(inp_str=''):
    """Посчитать буквы

    Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
    """
    inp_str1 = ''

    for i in inp_str:
        if i in ascii_letters:
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


def n_fibonacci(n=1):
    """Вывести n-ое число Фибоначчи."""
    f1 = 0
    f2 = 1
    i = 1

    if i != n:
        while i < n:
            f1, f2 = f2, f1 + f2
            i += 1

    print(f1)


def palindrome(number=0):
    """Определить, является ли число палиндромом."""
    a = 0
    c = number

    while c > 0:
        b = c % 10
        a = a * 10 + b
        c = c // 10

    if a == number:
        print("Это палиндром")
    else:
        print("Это НЕ палиндром")


def triangle(a=1, b=1, c=1):
    """Проверить, действительно ли это стороны треугольника."""
    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        square = square ** 0.5
        square = str(square)
        print("Это треугольник площадью " + square[:5])
    else:
        print("Это НЕ треугольник")


def solution(string=''):
    """Перевернуть строку."""
    print(string[::-1])


def descending_order(num=''):
    """Вывести числа в порядке убывания."""
    n = []
    for i in str(num):
        n.append(i)
    n.sort(reverse=True)
    n = ''.join(n)
    return n


def find_short(s=''):
    """Find shortest Word."""
    text1 = s.split()
    min_text = s
    for i in text1:
        if len(i) < len(min_text):
            min_text = i
    len_text = len(min_text)
    return len_text


def sort_array(source_array=[1, 2]):
    """Sort the odd.

    You will be given an array of numbers. You have to sort the odd numbers in
    ascending order while leaving the even numbers at their original positions
    """
    list_even = []
    new_list = source_array[:]

    for i in source_array:
        if i % 2 != 0:
            list_even.append(i)

    list_even.sort()
    a = 0

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            new_list[i] = list_even[a]
            a += 1
    return new_list


def fizzbuzz():
    """FizzBuzz

    Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
    кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
    одновременно кратных и 3 и 5 - FizzBuzz
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


def learn_list():
    """Генератор списка

    Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
    """
    lst = [first + second for first in 'ab' for second in 'bcd']
    print(lst)

    lst_2 = lst[::2]
    print(lst_2)

    lst_3 = [number + 'a' for number in '1234']
    print(lst_3)

    print(lst_3.pop(1))

    lst_4 = lst_3[:]
    lst_4.insert(1, "2a")
    print(lst_4)


def learn_tuple():
    """Создайте список ['a', 'b', 'c'] и сделайте из него кортеж"""
    lst = ['a', 'b', 'c']
    tpl = tuple(lst)
    print(tpl)

    tpl_1 = ('a', 'b', 'c')
    lst_1 = list(tpl_1)
    print(lst_1)

    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    tpl_2 = ([1, 2, 3],)
    for i in tpl_2[0]:
        print(i)
    print(len(tpl_2))


def list_number(input_string=''):
    """Посчитать пары

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
    другу. Считается, что любые два элемента, равные друг другу образуют одну
    пару, которую необходимо посчитать
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """
    lst = input_string.split()
    num = 0
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
            num += lst.count(i)
    print('Количество пар: ' + str(num))


def unique_elements(input_list=[1, 2, 3, 1, 1, 2, 4, 7, 'a', 'b', 'a']):
    """Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются в списке только
    один раз. Элементы нужно выводить в том порядке, в котором они встречаются
    в списке.
    """
    new_lst = []
    for i in input_list:
        if input_list.count(i) == 1:
            new_lst.append(i)
    print(new_lst)


def sort_list(input_list=[1, 0, 0, 2, 4, 1, 0, 4, 5, 0, 3, 7]):
    """Упорядоченный список.

    Дан список целых чисел. Требуется переместить все ненулевые элементы в
    левую часть списка, не меняя их порядок, а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя, дополнительный список
    использовать нельзя, задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.
    """
    for i in input_list:
        if i == 0:
            input_list.remove(i)
            input_list.append(i)
    print(input_list)


def dict_comprehensions():
    """Dict comprehensions

    Создайте словарь с помощью генератора словарей, так чтобы его ключами были
числа от 1 до 20, а значениями кубы этих чисел.
    """
    dictionary = {element: element ** 3 for element in range(1, 21)}

    print(dictionary)


def cities(num_country=1, country_city='Belarus Minsk', num_city=1,
           city='Minsk'):
    """ Города

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
                print(country)
            else:
                print('Страна неизвестна')


def two_list_number1():
    """Сравнить списки

    Даны два списка чисел. Посчитайте, сколько различных чисел содержится
    одновременно как в первом списке, так и во втором.
    """
    list_number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_number2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = set(list_number1) & set(list_number2)

    print(len(result))


def two_list_number2():
    """Сравнить списки

    Даны два списка чисел. Посчитайте, сколько различных чисел входит
    только в один из этих списков.
    """
    list_number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_number2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = set(list_number1) ^ set(list_number2)

    print(len(result))


def languages(num_schoolboy=1, num_lang=1, lang='Russian'):
    """ Языки

    Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
    языки знают все школьники и языки, которые знает хотя бы один из школьников
    Входные данные
    Первая строка входных данных содержит количество школьников N. Далее идет
    N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия
    языков, которые знает i-й школьник.
    Выходные данные
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки - список таких языков. Затем - количество языков,
    которые знает хотя бы один школьник, на следующих строках - список таких
    языков.
    """
    # Создать словарь: ключ = номер школьника, значение = список языков
    count1 = 1
    dict_schoolboy_lang = {}

    while count1 <= int(num_schoolboy):
        set_lang = set()
        count2 = 1
        while count2 <= int(num_lang):
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


def different_words(input_string='Hello!     How are you?\n'
                                 ' Where are you going?'):
    """ Слова

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

    print(f'В строке встречается {len(words)} различных слов')


def euclid_algorithm(num1=1, num2=2):
    """ Числа

    Даны два натуральных числа. Вычислите их наибольший общий делитель при
    помощи алгоритма Евклида (мы не знаем функции и рекурсию).
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    print(f'Общий делитель: {num1 + num2}')
