#BUBBLE SORT 

def bubble_sort(v):
    for i in range(len(v)-1): 
	    for j in range(len(v)-i-1): 
	        if(v[j] > v[j+1]):
                    v[j] = v[j+1]
                    v[j+1] = v[j]

exemplo = [25, 57, 48, 37, 12, 92, 86, 33]
bubble_sort(exemplo)
#Não funcionou.

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
insertion_sort(exemplo)

#MERGE SORT
#QUICK SORT
#HEAP SORT