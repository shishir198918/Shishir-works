l1=[]
flag=1
str1=""
for i in range(5):
    str1=input()
    l1.append(str1)
for j in range(len(l1)-1):
    if l1[j] in l1[j+1]:
        flag=True
    else:
        flag=False
        print("non magical")
        break
if flag:
    print("magical")
    
