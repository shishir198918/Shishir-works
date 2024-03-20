def factor(n):
    a=n//2
    l=[]
    for i in range(1,a,1):
        if n%i==0:
            l.append(i)
        
    return l
def main():
    a=int(input())
    b=int(input())
    l1=factor(a)
    l2=factor(b)
    l3=[]

    for i in l1:
        if i in l2:
            l3.append(i)
    if l3==[1]:
        print("Coprime")
    else:
        print("Not coprime")

main()        
