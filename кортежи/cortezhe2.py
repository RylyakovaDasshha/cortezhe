def slicer(tpl,element):
    #условие, которое проверяет есть ли элемент кортежа
    if element not in tpl:
        return()
        #кол-во вхождения элемента в кортеж
    if tpl.count(element)== 1:
        #функция возвращает отрезок кортежа начиная со вхождения элемента и до конца
        return (tpl[tpl.index(element):])
    elif tpl.count (element)==2:
        s = ''
        #цикл, который перебирает кортеж
        for i in tpl:
            #перенос содержания кортежа в строку s
           s += str(i)
            #возвращение отрезка кортежа начиная с 1 вхождения элемента заканчивая 2
        return tpl[s.index(str(element)):s.index(str(element))+1]
    
                   
        
