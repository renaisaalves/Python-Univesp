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
        x = v[i] #2º elemento / que está na posição 1
        j = i-1 #1º elemento / que está na posição 0
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
insertion_sort(exemplo)

#MERGE SORT

def intercala(v, ini, meio, fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    L.append(999) #sentinela
    R.append(999) #sentinela
    i = 0
    j = 0
    for k in range(ini, fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
            
def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio+1, fim)
        intercala(v, ini, meio, fim)
merge_sort(exemplo)

#QUICK SORT
def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    while i < j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)
quick_sort(exemplo)

#HEAP SORT

