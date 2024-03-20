s="asge,020"
b=0
for i in range(len(s)):
    if s[i].isnumeric():
        b=i
        break
print(b)    
if s[b:6].isnumeric():
    print("KAN KAR GAYA")
else :
    print("galat hai re")
    
  
    

