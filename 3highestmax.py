a={
    'a':50,
    'b':58,
    'c':56,
    'd':40,
    'e':100,
    'f':20}
max=0
second_max=0
third_max=0
for i in a:
    for j in a:
        if a[j]>max:
            max=a[j]
        elif a[j]>second_max and a[j]<max:
            second_max=a[j]
        elif a[j]>third_max and a[j]<second_max:
            third_max=a[j]
print(max)
print(second_max)
print(third_max)

 