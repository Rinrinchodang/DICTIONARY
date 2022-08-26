a=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
b={}
for i in a:
    for j in a:
        if i[0]==j[0]:
            b.update({i[0]:[j[1],i[1]]})
            break
print(b)

list=['one','two','three','four']
d={}
i=0
while i<len(list):
    # if list[i] not in d:
        d[i]=list[i]
        i+=1
print(d)
