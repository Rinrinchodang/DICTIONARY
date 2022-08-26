# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in a:
#     for j in a:
#         if a[j]>a[i]:
#             a[j],a[i]=a[i],a[j] 
# print(a)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in a:
#     for j in a:
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# b=sorted(a.values())
# print(b)
# c={}
# for i in b:
#     for j in a.keys():
#         if a[j]==i:
#             c[j]=i
# print(c)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# b=sorted(a.values())
# c={}
# for i in reversed(b):
#     for j in reversed(a.keys()):
#         if a[j]==i:
#             c[j]=i
# print(c)


b=[]
c={}
a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in a:
    d=a[i]
    b.append(d)
    j=0
    while j<len(b):
        k=0
        while k<len(b)-1:
            if b[k]>b[k+1]:
                b[k],b[k+1]=b[k+1],b[k]
            k+=1
        j+=1
i=0
while i<len(b):
    for key,value in a.items():
        if value==b[i]:
            c.update({key:value})
    i+=1
print(c)


