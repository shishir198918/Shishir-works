def cleaning ():
    a=input()
    l1=str(a.split("."))
    l1=str(a.split(";"))
    l1=str(a.split(","))
    l1=a.split(" ")
    l2=[".",";"]
    for i in l1:
        for j in l1:
            if j in i:
                i.replace(j,"")
                
            
    
    
    return(l1)


def counting(L,i):
    count=0
    
    for j in L:
        if j==i:
            count=count+1
    return count        
            
def dic():
    d=cleaning()
    dit={}
    a=0
    c=set(d)
    print(c)
    for i in c:
        dit[i]=counting(d,i)
    
    return(dit)    
        
print(dic())        
