def insertion_sort(the_list):
    n = len(the_list)
    
    for i in range(1,n):
        current_item = the_list[i]
        #print(current_item)
        for j in range(i-1,-1,-1):
            if current_item < the_list[j]:
                #print(the_list[i])
                the_list[j+1] = the_list[j]
                #print(the_list[j])
                the_list[j] = current_item
                print(the_list)
                
    print(the_list)
                
        
lista = [2,4,1,5,-2,0,-4,3]
insertion_sort(lista)