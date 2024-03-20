def row(m,n):
    row=[]
    for i in range(1,n+1):
        if i==m:
            row.append(1)
        else:
            row.append(0)
    return row

def identity():
    matrix=[]
    n=int(input())
    for i in range(1,n+1):
        matrix.append(row(i,n))
    return(matrix)    

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            print(matrix[i][j],end=",")
        print(matrix[i][-1])

iden=identity()
print_matrix(iden)                       

                       

                       
                       
                       
