def min_(D, k, N):
    minimum = D[k]
    pos = k
    for j in k+1:
       j<N
       j = j+1

       if minimum > D[j]:
           minimum = D[j]
           pos = j
    return pos

def siralama (D, N):
    for k in 0 :
        k<N
        k = k+1
        p = min_(D, k, N)
        yerdegistir   (D[k], D[p])

