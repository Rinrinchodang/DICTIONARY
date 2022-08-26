user=int(input("enter the number :"))
a={}
i=1
while i<=user:
    j=1
    b=[]
    while j<=10:
        b.append(i*j)
        a[i]=b
        j+=1
    i+=1
print(a,end=" ")

    
   