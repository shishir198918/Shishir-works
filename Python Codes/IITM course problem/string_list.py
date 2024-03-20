
def listed(a):
    l=[]
    b=""
    for i in a:
        l.append(i)
    if (len(a)%2==0) and l[-1]!=".":
        l.append(".")
    elif l[-1]==".":
        l.remove(l[-1])
       
    
    for j in l:
        b=b+j
    return b


def main():
    word=input()
    w1=listed(word)
    n=((len(w1)//2)+1)
    w2=w1[n-2:n+1]
    print(w2)
        

main()
print(len("abcdefghijk."))
