def mod(a):
    if a>=0:
        a=a
    else:
        a=a*(-1)
    return a

def sept(str1):
    a=int(str1[1])
    return a

def main():
    d={"A":1,"B":2,"C":3,"D":4,"D":4,"E":5,"F":6,"G":7,"H":8}
    start=input()
    end=input()
    if (mod(d[start[0]]-sept(start))==mod(d[end[0]]-sept(end))):
        print("YES")
    else:
        print("NO")
    
    

main()    
        
