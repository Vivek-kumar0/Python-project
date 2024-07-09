a=[1,2,4,5,6]
v=
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==v:
            print(i,j)
