def doubble(n):
    l=[]
    t=0
    for i in range(1,n,1):
        for j in range(1,n,1):
            if i<j:
                t=i,j
                l.append(t)
            
    return l

def squaresum(m):
    j=[]
    x=0
    for i in range(len(m)):
        x=(m[i][0])**2+(m[i][1])**2
        j.append(x)
    return j

def naturalsum(o):
    t=0
    l1=[]
    for i in range(1,o,1):
        t=i,i**2
        l1.append(t)
    return l1    
        
def main():
    a=int(input())
    t=0
    b="NO SOLUTION"
    l4=[]
    l1=doubble(a)
    l2=squaresum(l1)
    l3=naturalsum(a)
    for i in range(len(l2)):
        for j in range(len(l3)):
            if l2[i]==l3[j][1]:
                t=l1[i],l3[j][0]
                l4.append(t)
    if l4==[]:
        print("NO SOLUTION")
    else:
        for i in range(len(l4)):
            for j in range(0,1,1):
                for k in range(0,2,1):
                    print(l4[i][j][k],end=",")
                print(l4[i][1])    
                    

                
                
main()
    
