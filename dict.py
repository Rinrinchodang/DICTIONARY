d1={'a':100,'b':20,'c':50}
d2={'a':200,'d':90,'e':20}
for i in d1:
    if i in d2:
        d2[i]=d1[i]+d2[i]
d1.update(d2)
print(d1)
    