# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только
# один раз. Элементы нужно выводить в том порядке, в котором они встречаются
# в списке.

lst = [1, 2, 3, 1, 1, 2, 4, 7, 'a', 'b', 'a']
new_lst = []

for i in lst:
    if lst.count(i) == 1:
        new_lst.append(i)

print(new_lst)
