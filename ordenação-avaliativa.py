lista = [25, 57, 48, 37, 12, 92, 86, 33]

#BUBBLE SORT
def busca(v, chave=0): 
    for i in range(len(v)): 
        if chave == v[i]: 
            return i 
    return -1 
print(busca(lista))

#QUICK SORT
def ordena(v): 
    for i in range(1, len(v)): 
        chave = v[i] 
        j = i - 1 
        while j >= 0 and v[j] > chave: 
            v[j + 1] = v[j] 
            j -= 1 
        v[j + 1] = chave
    return v
print(ordena(lista))

