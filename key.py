# a={'a':2,'b':3,'c':14}
# for i in a:
#     print(i)

list=["243"]
i=0
while i <len(list):
    j=0
    while j<len(list[i]):
        a=int(list[i][j])*int(list[i][j])
        print(a,end="")
        j+=1
    i+=1

