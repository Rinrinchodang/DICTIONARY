# sol=([1,2,3,10,5])
# sol1=[]
# i=0
# while i<len(sol):
#     j=0 
#     while j<len(sol):
#         if sol[i]>sol[j]:
#             sol[i],[j]=sol[j],[i]
#         sol.append(sol1)
#         j+=1
#     i+=1
# print(sol1) 

def sol(num):
    i=0
    if num==None:
        return[]
    while i<len(num)-1:
        if num[i]>num[i+1]:
            num[i],num[i+1]=num[i+1],num[i]
        i+=1
    return num
print(sol(None))
    
