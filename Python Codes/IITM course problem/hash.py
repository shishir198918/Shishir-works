def list_n():
    #verified 
    n=int(input())
    l=[]
    a=""
    for i in range(n):
        a=input("item of list  ")
        l.append(a)
    return l

def hash(l):
    #verified 
    lin=0
    for i , j in zip(range(len(l)),range(1,(len(l)+1))):
        a=ord(l[i])
        lin=lin+((a*j)/10)
    return lin    
        
def hash_table(l):
    d={}
    for i in l:
        
        d[i]=hash(i)
    return d    
a=list_n()
b=hash_table(a)
print(a,b)
