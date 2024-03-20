num=int(input("Write a number: "))
abs_num=abs(num)
rev=abs_num%10
abs_num=abs_num//10
while(abs_num>0):
    r=abs_num%10
    abs_num=abs_num//10
    rev=rev*10+r
if(num>0):
    print(rev)

else:
    print(rev*(-1))
    
if(rev==abs_num):
    print("number is palidrome:")

