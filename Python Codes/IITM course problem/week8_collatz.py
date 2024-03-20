def collatz(n):
    m=0
    if n==1:
        return m
    if n%2==0:
        m=m+1
        return (1+ collatz(n/2))
    else:
        m=m+1
        return (1+collatz(n*3+1))

print(collatz(7))
        
