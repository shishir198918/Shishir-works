def row(n):
    a=0
    x=[]
    l=input().split(",")
    for i in range(len(l)):
        a=int(l[i])
        x.append(a)
    return x    
    
    
    
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(row(n))
print(matrix)    
        

