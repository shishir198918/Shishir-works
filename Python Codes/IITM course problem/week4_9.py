def row(n):
    a=0
    x=[]
    l=input().split(" ")
    for i in range(len(l)):
        a=int(l[i])
        x.append(a)
    return x    
    
    
def main():
    n=int(input())
    mat=[]
    
    for i in range(n):
        mat.append(row(n))
    a=int(input())    
    for j in range(len(mat)):
        for k in range(len(mat[j])):
            mat[j][k]=a*mat[j][k]
    return mat


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            print(matrix[i][j],end=",")
        print(matrix[i][-1])

    
        
