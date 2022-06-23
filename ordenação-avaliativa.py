lista = [25, 57, 48, 37, 12, 92, 86, 33]

#BUBBLE SORT
def busca(v, chave=0): 
    for i in range(len(v)): 
        if chave == v[i]: 
            return i 
    return -1 
print(busca(lista))

#QUICK SORT
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

#
def ordena1(v): 
    n = len(v) 
    for i in range(n): 
        for j in range(n - i - 1): 
            if v[j] > v[j + 1]: 
                v[j], v[j + 1] = v[j + 1], v[j]
    return v
print(ordena1(lista))
