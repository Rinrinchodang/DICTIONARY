


p={2:5,3:6,6:7,8:4}
x=[]
for i in p:
    x.append(p[i])
    j=0
    m=0
    for j in x:
        if j>m:
            m=j
print(m)