def reverse(L):
    if len(L)==1:
        return L
    else:
        m=L[0]
        L.remove(m)
        return reverse(L)+[m]
print(reverse([(1, 2), (3, 4), (5, 6), (7, 8)]))
