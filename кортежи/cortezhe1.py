def tpl_sort(tpl):
    for i in tpl:
        #функция проверяет является ли число целым
        if not isinstance(i, int):
            #если не является целым, то переходит в исходный список
           return tpl
            #остортированный кортеж
    resulf = (sorted(tpl))
    return resulf
    
tpl = (1, 8, 9, 7)
print(tpl_sort(1,8.2.5,7))
