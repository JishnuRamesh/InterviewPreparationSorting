
def merge_sort(lista,start,end):
    if start < end:
        middle = (start+end)//2;
        merge_sort(lista, start, middle)
        merge_sort(lista, middle+1, end)
        merge(lista,start,middle,end)
        
        
def merge(lista,start,middle,end):
    left = lista[start:middle+1]
    right = lista[middle+1:end+1]

    i = j = 0
    
    for k in range(start, end+1):
        if (i < len(left) and j < len(right)):

            if left[i] <= right[j]:
                lista[k] = left[i]
                i += 1
                
            else :
                lista[k] = right[j]
                j += 1
                
        elif i < len(left):
            lista[k] = left[i]
            i += 1
            
        else:
            lista[k] = right[j]
            j += 1
            
    print(lista)
    
            

    #print(lista)

lista = [2,4,1,5,-2,0,-4,3]
merge_sort(lista, 0, len(lista)-1)
    