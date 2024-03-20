alpha="abcdefghijklmnopqrstuvwxyz"
coded=""
name=input("Write something want to encrypte ")
for i in range(len(name)):
    coded=coded+alpha[((alpha.index(name[i])+1)%26)]
    

print(coded)    
