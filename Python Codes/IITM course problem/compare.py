marks=[3,6,8,1,2,10,10,4]
st1=marks[0]
st2=marks[1]
comp=0
inter=0
for i in range(len(marks)):
    if comp<marks[i]:
        comp=marks[i]
        st2=comp
        if st1<st2:
            inter=st1
            st1=st2
            st2=inter
print(st1)
print(st2)
