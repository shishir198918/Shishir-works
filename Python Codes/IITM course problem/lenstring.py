def userinput():
    a=""
    l=[]
    d={}
    while(a!="abcdefghijklmnopqrstuvwxyz"):
        a=input()
        l.append(a)
    for i in l:
        d[i]=len(i)
    return d


def minimum(l):
    a=list(l.items())
    b=26
    c=""
    for i in range(len(a)):
        if b>a[i][1]:
            b=a[i][1]
            c=a[i][0]

    return c       
    
x=userinput()
print(minimum(x))
