exemplo = [25, 57, 48, 37, 12, 92, 86, 33]

#BUBBLE SORT 
def bubble_sort(v):
    for i in range(len(v)-1): 
	    for j in range(len(v)-i-1): 
	        if(v[j] > v[j+1]):
                    v[j], v[j+1] = v[j+1], v[j]
    return v
bubble = bubble_sort(exemplo)
print(bubble, 'Bubble Sort')
#Não funcionou.

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i] #2º elemento / que está na posição 1
        j = i-1 #1º elemento / que está na posição 0
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
    return v
insertion = insertion_sort(exemplo)
print(insertion, 'Insertion Sort')

#MERGE SORT

           
'''def merge_sort(v, ini=0, fim=len(v)-1):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio+1, fim)
        intercala(v, ini, meio, fim)
    return v
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
    return v '''

#QUICK SORT
def quick_sort(v, ini=0, fim=0):
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
    return v
quick = quick_sort(exemplo)
print(quick, 'Quick Sort')

#HEAP SORT