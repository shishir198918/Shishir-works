def row(n):
    a=0
    x=[]
    l=input().split(",")
    for i in range(len(l)):
        a=int(l[i])
        x.append(a)
    return x    
    
    
def matrix(n):
    
    mat=[]
    
    for i in range(n):
        mat.append(row(n))  
    return mat

def blank_matrix(n):
    blank=[]
    row=[]
    for i in range(n):
        blank.append(row)
    return blank

    

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            print(matrix[i][j],end=",")
        print(matrix[i][-1])

def main():
    n=int(input())
    A=blank_matrix(n)
    B=matrix(n)
    C=matrix(n)
    print(A)

    for i in range(n):
        for j in range(n):
            a=(B[i][j]+C[i][j])
            A[i].append((a))
            print(i,j,A[i][j])
    return A

print(main())    






















    
    
