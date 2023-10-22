def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i, int):
           return tpl
    resulf = (sorted(tpl))
    return resulf
    
tpl = (1, 8, 9, 7)
print(tpl_sort(tpl))