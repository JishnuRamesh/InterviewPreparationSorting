def bubble_sort(the_list):
    n = len(the_list)
    
    for i in range(n-1,0,-1):
        for j in range(i):
            if the_list[j] > the_list[j+1]:
                temp = the_list[j]
                the_list[j] = the_list[j+1]
                the_list[j+1] = temp
                
    print(the_list)
                
lista = [2,4,1,5,-2]
bubble_sort(lista)