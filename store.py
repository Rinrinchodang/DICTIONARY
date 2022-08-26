dic=[{"first":"1"},{"second":"2"},{"third":"1"},{"four":"5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
a=[]

# for i in a:
#     if i not in a:
#         b.append(i)
# print(b)
while i <len(dic):
    for j in dic[i]:
        if dic[i][j] not in a:
            # a.append(a[i])
            a.append(dic[i][j])
    i+=1
print(a)