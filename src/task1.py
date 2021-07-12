""" Оформите решение задач из прошлых домашних работ в функции. Напишите
 функцию runner. (все станет проще когда мы изучим модули, getattr и setattr).
 a. runner() – все фукнции вызываются по очереди
 b. runner(‘func_name’) – вызывается только функцию func_name.
 c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def total_price():  # hw1 t1
    rub = int(input("Укажите стоимость, руб: "))
    penny = int(input("Укажите стоимость, коп: "))
    q = int(input("Укажите количество: "))

    price_q = (rub * 100 + penny) * q
    price_rub = price_q // 100
    price_penny = price_q % 100

    print("Общая ст-ть: " + str(price_rub) + "руб. " + str(price_penny) +
          "коп.")


def longest_word():  # hw1 t2
    text = input("Введите текст: ")
    punctuation = ',.:;-_!?'

    for i in text:
        if i in punctuation:
            text = text.replace(i, '')

    text1 = text.split()
    max_text = ''
    for i in text1:
        if len(i) > len(max_text):
            max_text = i

    print(max_text)


def del_spaces():  # hw1 t3
    inp_text = input("Введите текст: ")

    inp_text = inp_text.replace(' ', '')
    n_text = ''

    for i in inp_text:
        if i not in n_text:
            n_text = n_text + i

    print(n_text)


def lower_upper():  # hw1 t4
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


def n_fibonacci():  # hw1 t5
    n = int(input("Введите n-е число Фибоначчи: "))

    f1 = 0
    f2 = 1
    i = 1

    if i != n:
        while i < n:
            f1, f2 = f2, f1 + f2
            i += 1

    print(f1)


def palindrome():  # hw1 t6
    input_ = int(input("Введите число: "))

    a = 0
    # b = 0
    c = input_

    while c > 0:
        b = c % 10
        a = a * 10 + b
        c = c // 10

    if a == input_:
        print("Это палиндром")
    else:
        print("Это НЕ палиндром")


def triangle():  # hw1 t7
    a = int(input("Введите 1-ую сторону: "))
    b = int(input("Введите 2-ую сторону: "))
    c = int(input("Введите 3-ую сторону: "))

    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        square = square ** 0.5
        square = str(square)
        print("Это треугольник площадью " + square[:5])
    else:
        print("Это НЕ треугольник")


def solution(string):  # hw1 t8_1
    print(string[::-1])


def descending_order(num):  # hw1 t8_2
    n = []
    for i in str(num):
        n.append(i)
    n.sort(reverse=True)
    n = ''.join(n)
    return int(n)


def find_short(s):  # hw1 t8_3
    text1 = s.split()
    min_text = s
    for i in text1:
        if len(i) < len(min_text):
            min_text = i
    len_text = len(min_text)
    return len_text


def sort_array(source_array):  # hw1 t8_4
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


def restaurant(single_tables, double_tables, visitors):  # hw1 t8_5
    lost_visitors = []
    half_double_tables = 0

    for i in visitors:
        if i == 1 and single_tables > 0:
            single_tables -= 1
        elif i == 1 and double_tables > 0:
            double_tables -= 1
            half_double_tables += 1
        elif i == 1 and half_double_tables > 0:
            half_double_tables -= 1
        elif i == 2 and double_tables > 0:
            double_tables -= 1
        else:
            lost_visitors.append(i)
    return sum(lost_visitors)


def fizzbuzz():  # hw3 t1
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


def learn_list():  # hw3 t2
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


def learn_tuple():  # hw3 t3
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


def list_number():  # hw3 t4
    str_ = input('Введите числа через пробел: ')
    lst = str_.split()
    num = 0
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
            num += lst.count(i)
    print('Количество пар: ' + str(num))


def unique_elements():  # hw3 t5
    lst = [1, 2, 3, 1, 1, 2, 4, 7, 'a', 'b', 'a']
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    print(new_lst)


def sort_list():  # hw3 t6
    lst = [1, 0, 0, 2, 4, 1, 0, 4, 5, 0, 3, 7]
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    print(lst)


def dict_comprehensions():  # hw4 t1
    dictionary = {element: element ** 3 for element in range(1, 21)}

    print(dictionary)


def cities():  # hw4 t2
    # Создать словарь: ключ = страна, значение = список городов
    num_country = input('Введите количество стран: ')
    count1 = 1
    dict_country = {}

    while count1 <= int(num_country):
        country_city = input('Введите страну и ее города: ')
        dict_country[country_city.split()[0]] = country_city.split()[1:]
        count1 += 1

    # Создать список запрашиваемых городов
    num_city = input('Введите количество запросов: ')
    count2 = 1
    list_city = []

    while count2 <= int(num_city):
        city = input('Введите город: ')
        list_city.append(city)
        count2 += 1

    # Проверить по каждому городу вхождение в словарь и вывести название страны
    for city in list_city:
        for country in dict_country:
            if city in dict_country.get(country):
                print(country)
            else:
                print('Страна неизвестна')


def two_list_number1():  # hw4 t3
    list_number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_number2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = set(list_number1) & set(list_number2)

    print(len(result))


def two_list_number2():  # hw4 t4
    list_number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_number2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = set(list_number1) ^ set(list_number2)

    print(len(result))


def languages():  # hw4 t5
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


def different_words():  # hw4 t6
    input_sting = 'Hello!     How are you?\n Where are you going?'
    punctuation = '!()-[]{};?:,.;_'
    edit_string = ''

    for element in input_sting:
        if element in punctuation:
            edit_string = input_sting.replace(element, '')

    words = set(edit_string.split())

    print(f'В строке встречается {len(words)} различных слов')


def euclid_algorithm():  # hw4 t7
    num1 = int(input('Введите первое натуральное число: '))
    num2 = int(input('Введите второе натуральное число: '))

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    print(f'Общий делитель: {num1 + num2}')


func_dict = {
    'total_price': total_price,
    'longest_word': longest_word,
    'del_spaces': del_spaces,
    'lower_upper': lower_upper,
    'n_fibonacci': n_fibonacci,
    'palindrome': palindrome,
    'triangle': triangle,
    'solution': solution,
    'descending_order': descending_order,
    'find_short': find_short,
    'sort_array': sort_array,
    'restaurant': restaurant,
    'fizzbuzz': fizzbuzz,
    'learn_list': learn_list,
    'learn_tuple': learn_tuple,
    'list_number': list_number,
    'unique_elements': unique_elements,
    'sort_list': sort_list,
    'dict_comprehensions': dict_comprehensions,
    'cities': cities,
    'two_list_number1': two_list_number1,
    'two_list_number2': two_list_number2,
    'languages': languages,
    'different_words': different_words,
    'euclid_algorithm': euclid_algorithm
}


def runner(*args):
    if not args:
        for func in func_dict.values():
            func()
    else:
        for element in args:
            func = func_dict.get(element)
            func()


# runner()
# runner('total_price')
# runner('total_price', 'longest_word', 'languages')
