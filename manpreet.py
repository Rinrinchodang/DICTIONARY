dic={101:"ram",102:"sham"}
for i in dic:
    print(i,":",dic[i])

dic={"ball":2,"cat":3}
for i in dic:
    print(i)
    break

dic={1:3,2:2}
user=int(input("enter any:"))
for i in dic:
    if i==user:
        print("correct")
    else:
        print("wrong")

