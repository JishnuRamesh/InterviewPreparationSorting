import sys

def qsort(lista):
    
    #print(sys.getrecursionlimit())
    
    if len(lista) <= 1:
        return lista
    
    else:
        return qsort([x for x in lista[1:] if x < lista[0]]) + [lista[0]] + qsort([x for x in lista[1:] if x >= lista[0]])
    
    
    
lista = [2,4,1,5,-2,0,-4,3]
qsorta = qsort(lista)
print(qsorta)
    
    