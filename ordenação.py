def bubble_sort(* v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                v[j] = v[j+1]
                v[j+1] = v[j]
vetor = (25, 57, 48, 37, 12, 92, 86, 33)
bubble_sort(vetor)
