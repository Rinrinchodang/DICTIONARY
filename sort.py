dic={1:2,3:4,4:3,2:1,0:0}
# for i in dic:
#     for j in dic:
#         if dic[j]>dic[i]:
#             dic[j],dic[i]=dic[i],dic[j]
# print(dic)

b=sorted(dic.keys())
# print(b)
c={}
for i in b:
    for j in dic.values():
        if dic[j]==i:
            c[j]=i
print(c)