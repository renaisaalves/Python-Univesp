lista = [25, 57, 48, 37, 12, 92, 86, 33]

#
def busca(v, chave=0): 
    for i in range(len(v)): 
        if chave == v[i]: 
            return i
    return -1
print(busca(lista))

#
def ordena4(v): 
    for i in range(1, len(v)): 
        chave = v[i] 
        j = i - 1 
        while j >= 0 and v[j] > chave: 
            v[j + 1] = v[j] 
            j -= 1 
        v[j + 1] = chave
    return v
print(ordena4(lista))

#
def ordena3(v): 
    from random import randint 
    if len(v) < 2: 
        return v 
    l, p, h = [], [], [] 
    ch = v[randint(0, len(v) - 1)] 
    for x in v: 
        if x < ch: 
            l.append(x) 
        elif x == ch: 
            p.append(x) 
        elif x > ch: 
            h.append(x) 
    return ordena3(l) + p + ordena3(h)
print(ordena3(lista))

#
def func(l, r): 
    if len(l) == 0: 
        return r 
    if len(r) == 0: 
        return l 
    res = [] 
    idx_l = idx_r = 0 
 
    while len(res) < len(l) + len(r): 
        if l[idx_l] <= r[idx_r]: 
            res.append(l[idx_l]) 
            idx_l += 1 
        else: 
            res.append(r[idx_r]) 
            idx_r += 1 
 
        if idx_r == len(r): 
            res += l[idx_l:] 
            break 
 
        if idx_l == len(l): 
            res += r[idx_r:] 
            break 
    return res 
 
def ordena2(v): 
    if len(v) < 2: 
        return v 
    meio = len(v) // 2 
    return func( 
        l = ordena2(v[:meio]), 
        r = ordena2(v[meio:]))
print(ordena2(lista))

#BUBBLE SORT 
def ordena1(v): #A lista original vai entrar na função
    n = len(v) #len vai contar quantos elementos existem na lista (há 8 elementos na lista) e jogar na variável n
    for i in range(n): #i vai rodar 8 linhas, começando na linha 0
        for j in range(n - i - 1): #j vai rodar a coluna 8-1 -1, ou seja, 8-0 = 8-1 = 7
            if v[j] > v[j + 1]: #exemplo: 25 > 57
                v[j], v[j + 1] = v[j + 1], v[j] #se um n for > que o outro, então trocam de posições
    return v
print(ordena1(lista), 'Bubble Sort')

#
def busca(v, i=0, f=0, chave=0): 
    if f < i: 
        return -1 
    m = (i + f) // 2 
    if v[m] == chave: 
        return m 
    if chave < v[m]: 
        return busca(v, i, m - 1, chave) 
    else: 
        return busca(v, m + 1, f, chave)
print(busca(lista))
