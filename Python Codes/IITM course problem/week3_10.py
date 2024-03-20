def userinput():
    n=0
    while(n<=0):
        n=int(input())
    return n

def prime(n):
    l=[]
    a=n//2
    for i in range(1,a+1,1):
        if n%i==0:
            l.append(i)
    if l==[1]:
        return n
    else:
        return 0
        
def listprime(m):
    l1=[]
    a=0
    for i in range(1,m+1,1):
        a=prime(i)
        l1.append(a)
    return l1    
        

def main():
    n=userinput()
    sum=0
    l2=listprime(n)
    for i in l2:
        sum=sum+i
    print(sum)    
main()
