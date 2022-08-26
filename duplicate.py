dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dic1=[]
x=dict()
for i,j in dic.items():
    if j not in dic1:
        dic1.append(j)
        x[i]=j
print(x)