dic={101:"Ram",102:"Sham"}
b={}
for j in dic:
    x=dic[j]
    i=-1
    c=[]
    while i>=-len(x):
        c.append(x[i])
        i-=1
    b[j]=c
print(b)