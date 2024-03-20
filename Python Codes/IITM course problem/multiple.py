def userinput():
    a=0
    while(a<=0):
        a=int(input())
    return a

def multiple(a,nrange,mrange):
    l=[]
    l2=[]
    if nrange%a==0:
        b1=int(nrange/a)# for boundary limit condition
    else:
        b1=int((nrange+(a-(nrange%a)))/a)
    b2=int((mrange-(mrange%a))/a)
    l=range(b1,b2+1,1)
    for i in range(len(l)):
        b=l[i]*a
        l2.append(b)
        
    return l2
def sum1(a,b,nrange,mrange):
    l5=[]
    s=0
    l3=multiple(a,nrange,mrange)
    l4=multiple(b,nrange,mrange)
    for i in l3:
        if i in l4:
            l5.append(i)
           
    for i in l5:
        s=s+i
        
    return s


def main():
    a=userinput()
    b=userinput()
    s1=sum1(a,b,1000,2000)
    print(s1)
    
main()

        
    
        
        
    
    
