def Linear(P,Q,K):
    if len(P)==0:
        return True
    if P[0]==K*Q[0]:
        P.remove(P[0])
        Q.remove(Q[0])

        return Linear(P,Q,K)
    else:
        return False
print(Linear([10, 20, 30, 40, 50],
[1, 2, 3, 4, 6],
10))
