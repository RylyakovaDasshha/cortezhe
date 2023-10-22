def slicer(tpl,element):
    if element not in tpl:
        return()
    if tpl.count(element)== 1:
        return (tpl[tpl.index(element):])
    elif tpl.count (element)==2:
        s = ''
        for i in tpl:
           s += str(i)
        return tpl[s.index(str(element)):s.index(str(element))+1]
    
                   
        
