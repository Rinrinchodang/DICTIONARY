# dic={2:5,6:1,5:4,1:4}
# mul=1
# for i in dic:
#     mul*=dic[i]
# print(mul)

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)    
for i in dic1:
    if i in dic2:
        dic2[i]=dic1[i]+dic3[i]
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

    