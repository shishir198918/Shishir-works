def user():
    l=[]
    a=0
    for i in range(4):
        a=int(input())
        l.append(a)
    return l

def mimm(l):
    m=l[0]
    for i in range(len(l)):
        if l[i]<m:
            m=l[i]

    return m

def printing(l):
    a=0
    for i in range(len(l)-1):
        
        a=l[i]
        print(a,end=" ")
    print(l[-1])    
        
def sorting():
    l1=user()
    l2=[]
    
    while(len(l1)>0):
        m=mimm(l1)
        l2.append(m)
        l1.remove(m)
    return l2    
a=sorting()
printing(a)
