a={"key1":22,"ww2":66,"key2":6}
user=int(input("enter any number"))
# b=[]
# b.append(a)
# if user=="22" and user=="66" and user=="6":
#     print("exist") 
# else:
#     print("not exist")
for i in a:
    if user==a[i]:
        print("exist")
    else:
        print("not exist")