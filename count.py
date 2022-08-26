a='w3school'
count={'w':0,'3':0,'s':0,'c':0,'h':0,'o':0,'l':0}
for i in a:
    if i=="w":
        count["w"]+=1
    elif i=="3":
        count["3"]+=1
    elif i=="s":
        count["s"]+=1
    elif i=="c":
        count["c"]+=1
    elif i=="h":
        count["h"]+=1
    elif i=="o":
        count["o"]+=1
    else:
        count["l"]+=1
print(count)

