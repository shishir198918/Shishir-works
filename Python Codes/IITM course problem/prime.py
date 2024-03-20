def user():
    n=1
    while(n<=1):
        n=int(input())
    return n
def fact(n):
    a=n//2
    l1=[]
    l=range(1,a+1,1)
    for i in l:
        if n%i==0:
            l1.append(i)
    return l1
print(fact(2))
def main():
    n=user()
    m=fact(n)
    if m==[1]:
        print("PRIME")
    else:
        print("NOT PRIME ")
main()        
