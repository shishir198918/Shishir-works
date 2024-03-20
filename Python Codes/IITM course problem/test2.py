while True:
    i=0
    try:
        a=input("Item:").title()
        b=[]
        
    except EOFError:
        break
    else :
        b.append(a[i])
        i=i+1
    
print(b)
