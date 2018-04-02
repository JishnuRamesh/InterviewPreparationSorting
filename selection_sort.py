def selection_sort(the_list):
    n = len(the_list)
    
    for i in range(n-1):
        smallest = i
        for j in range(i+1,n):
            if the_list[j] < the_list[smallest]:
                smallest = j 
                
        the_list[smallest],the_list[i] = the_list[i],the_list[smallest]

    print(the_list)
        
lista = [2,4,1,5,-2]
selection_sort(lista)