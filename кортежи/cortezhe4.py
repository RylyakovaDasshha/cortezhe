def del_from_tuple(tup, value):
    lst = list(tup)
    lst.remove(value)
    return tuple(lst)

tup = (1, 2, 3, 2, 4, 2)
value = 2

new_tup = del_from_tuple(tup, value)
print(new_tup)
