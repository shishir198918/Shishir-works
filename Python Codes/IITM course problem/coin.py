#entering the function
def userinput():
    d={"coin":0,"s1":0,"s2":0,"s3":0}
    for i in d:
        while(d[i]<=0):
            d[i]=int(input())
    return d

def fair():
    d=userinput()
    
    if (d["coin"]==d["s1"]+d["s2"]+d["s3"])and (d["s1"]!=d["s2"]!=d["s3"]):
        print("FAIR")
    else:
        print("UNFAIR")
        
 
        
fair()
