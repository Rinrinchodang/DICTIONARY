i=0
a=[]
b=[]
while i<=10:
    user1=input("enter the name")
    user2=int(input("enyter the mark"))
    a.append(user1)
    b.append(user2)
    j=0
    dic={}
    while j<len(a) and j<len(b):
        dic[a[j]]=b[j]
    i+=1
print(dic)