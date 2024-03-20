def userinput():
    a=0
    while(a<=0):
        a=int(input())

    return a

n=userinput()
a=n//2
for i in range(1,a+1,1):
    if n%i==0:
        print(i)
        
