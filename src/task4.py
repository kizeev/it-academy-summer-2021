""" В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data_hw5/ ratings.list.
 a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
 b. Найдите ТОП250 фильмов и извлеките заголовки.
 c. Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt
    – гистограмма рейтингов, years.txt – гистограмма годов.
"""


try:
    with open('data_hw5/ratings.list', encoding='ISO-8859-1') as input_list:

        lines = input_list.readlines()
        start_line = 'New  Distribution  Votes  Rank  Title\n'
        end_line = 'BOTTOM 10 MOVIES (1500+ VOTES)\n'
        top250_list = []
        rating_list = []
        year_list = []
        is_read = False

        for line in lines:
            if not is_read and line != start_line:
                continue
            if line == end_line:
                break
            is_read = True
            if line != start_line and line != '\n':
                edit_line = line.split()[2:]
                rating = edit_line[0]
                movie = ' '.join(edit_line[1:-1])
                year = edit_line[-1]
                top250_list.append(movie)
                rating_list.append(rating)
                year_list.append(year[1:5])

    input_list.close()

    for movie in top250_list:
        print(movie)

    with open('top250_movies.txt', 'w') as top250_movies:
        for movie in top250_list:
            top250_movies.write(movie + '\n')

    top250_movies.close()

    with open('ratings.txt', 'w') as ratings:
        bar_char_rating = {rating: rating_list.count(rating)
                           for rating in rating_list
                           }
        for key, value in bar_char_rating.items():
            ratings.write(f'Количество фильмов с рейтингом {key}: {value}\n')

    ratings.close()

    with open('years.txt', 'w') as years:
        year_list.sort()
        bar_char_years = {year: year_list.count(year) for year in year_list}
        for key, value in bar_char_years.items():
            years.write(f'В {key} году вышло фильмов: {value}\n')

    years.close()


except FileNotFoundError:
    print('Файл не существует')
