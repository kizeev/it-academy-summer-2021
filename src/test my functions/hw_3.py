def unique_elements(input_list):
    """Уникальные элементы в списке
    Дан список. Выведите те его элементы, которые встречаются в списке только
    один раз. Элементы нужно выводить в том порядке, в котором они встречаются
    в списке.
    """
    new_lst = []
    for i in input_list:
        if input_list.count(i) == 1:
            new_lst.append(i)
    return new_lst


def sort_list(input_list):
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
    return input_list