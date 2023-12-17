def del_from_tuple(tup, value):
    #кортеж переводим в список
    lst = list(tup)
    #из списка удаляем элемент
    lst.remove(value)
    #список переводим в кортеж и возвращаем его
    return tuple(lst)
#создаем кортеж
tup = (1, 2, 3, 2, 4, 2)
#создаем переменную
value = 2
#создаем переменную со значением функции которая описывает 1-7 строчку
new_tup = del_from_tuple(tup, value)
#выводим значение переменной
print(new_tup)
