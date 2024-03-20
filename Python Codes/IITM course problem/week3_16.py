

def line():
    mark=int(input())
    No_options=int(input())
    v=mark/No_options
    
    correct_options=input()
    c2=correct_options.split(",")
    
    user_options=input()
    u2=user_options.split(",")
    c1=set(c2)
    u1=set(u2)
    if u1.issubset(c1):
        m=u1.intersection(c1)
    else:
        m={}

    marks=len(m)*(v)
    print(marks)

line()    
